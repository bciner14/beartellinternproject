using UnityEngine;
using UnityEngine.UI;
using TMPro;
using OpenAI;
using UnityEngine.Events;
using System.Threading.Tasks;
using System.IO;
using System.Collections.Generic;

public class AIChatManager : MonoBehaviour
{
    public OnResponseEvent OnResponse;

    public UnityEvent OnChatPaused = new UnityEvent();

    [System.Serializable]
    public class OnResponseEvent : UnityEvent<string> { }

    private OpenAIApi openAI = new OpenAIApi();
    private List<ChatMessage> messages = new List<ChatMessage>();
    private bool awaitingPCValues = false;
    private bool isChatPaused = false;

    public TMP_InputField userInputField;
    public Button submitButton;
    public TextMeshProUGUI chatText;
    public Button saveButton;
    public Button findInDirectoryButton;

    private string savePath;
    private string directoryPath; 

    void Start()
    {
        submitButton.onClick.AddListener(SubmitUserInput);
        saveButton.onClick.AddListener(SaveConversation);
        findInDirectoryButton.onClick.AddListener(FindInDirectory);
    }

    public void SaveConversation()
    {
        string conversationText = FormatConversationForSaving();
        File.WriteAllText(savePath, conversationText);
        Debug.Log("Conversation saved to: " + savePath);
    }

    private string FormatConversationForSaving()
    {
        string conversationText = "";
        foreach (var message in messages)
        {
            conversationText += $"{message.Role}: {message.Content}\n";
        }
        return conversationText;
    }

    public void GetSavePathAndSave()
    {
        savePath = GetSavePath();
        SaveConversation();
    }

    private string GetSavePath()
    {
        string fileName = "conversation.txt";
        string folderName = "ChatSaveFolder"; 
        string folderPath = Path.Combine(Application.dataPath, folderName);

        if (!Directory.Exists(folderPath))
        {
            Directory.CreateDirectory(folderPath);
        }

        string path = Path.Combine(folderPath, fileName);
        return path;
    }

    public void FindInDirectory()
    {
        string folderPath = "Assets/ChatSaveFolder"; 
        UnityEditor.EditorUtility.RevealInFinder(folderPath); 
        Debug.Log("Opened directory: " + folderPath);
    }

    public async void AskChatGPT(string newText)
    {
        if (!isChatPaused)
        {
            ChatMessage newMessage = new ChatMessage();
            newMessage.Content = newText;
            newMessage.Role = "user";

            if (awaitingPCValues)
            {
                HandleUserPCValuesInput(newMessage);
            }
            else
            {
                messages.Add(newMessage);

                CreateChatCompletionRequest request = new CreateChatCompletionRequest();
                request.Messages = messages;
                request.Model = "gpt-3.5-turbo";

                var response = await openAI.CreateChatCompletion(request);

                if (response.Choices != null && response.Choices.Count > 0)
                {
                    var chatResponse = response.Choices[0].Message;
                    messages.Add(chatResponse);

                    Debug.Log(chatResponse.Content);

                    if (newText.ToLower() == "mpcv")
                    {
                        awaitingPCValues = true;
                        OnResponse.Invoke("We are getting your PC values. When the chat has all the values, press 'Submit' or use the keyboard Enter key to continue.");
                        return;
                    }
                }
            }

            UpdateConversationDisplay();
        }
        else
        {

        }
    }
    private void HandleUserPCValuesInput(ChatMessage userMessage)
    {
            
            string pcResponse = $"Thank you for providing the PC values: {userMessage.Content}";
            awaitingPCValues = false;

            ChatMessage pcResponseMessage = new ChatMessage();
            pcResponseMessage.Content = pcResponse;
            pcResponseMessage.Role = "assistant";
            messages.Add(pcResponseMessage);

            OnResponse.Invoke(pcResponse);

            OnChatPaused.Invoke();
        
    }

    public void SubmitUserInput()
    {
        string userText = userInputField.text;

        if (!string.IsNullOrEmpty(userText))
        {
                AskChatGPT(userText);
                userInputField.text = ""; 
        }

        if (awaitingPCValues && (userText.ToLower() == "enter" || userText.ToLower() == "submit"))
        {
            awaitingPCValues = false; 
            userInputField.text = ""; 
        }
        else
        {
            AskChatGPT(userText);
            userInputField.text = "";
        }
        if (!string.IsNullOrEmpty(userText))
        {
            if (userText.ToLower() == "mpcv")
            {
            
                isChatPaused = true;
                OnResponse.Invoke("We are getting your PC values. When the chat has all the values, press 'Submit' or use the keyboard Enter key to continue.");
                userInputField.text = ""; 
            }
            else if (isChatPaused && (userText.ToLower() == "enter" || userText.ToLower() == "submit"))
            {
                
                isChatPaused = false;
                userInputField.text = ""; 
            }
            else
            {
                AskChatGPT(userText);
                userInputField.text = "";
            }
        }
    }


    private void UpdateConversationDisplay()
    {
        string conversationText = "";
        foreach (var message in messages)
        {
            conversationText += $"{message.Role}: {message.Content}\n";
        }
        chatText.text = conversationText;
    }
}
