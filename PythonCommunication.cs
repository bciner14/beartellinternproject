using System.Collections;
using System.Collections.Generic;
using System.Net;
using UnityEngine;
using UnityEngine.Networking;

[System.Serializable]
public class SQLQuery
{
    public string sql_query;
}

public class PythonCommunication : MonoBehaviour
{
    private string serverURL = "https://192.168.110.104:5000/execute_sql";
    private string sqlQuery = "SELECT * FROM pcutility";

    public AIChatManager chatManager;

    private void Start()
    {
        // Subscribe to the OnChatPaused event
        if (chatManager != null)
        {
            chatManager.OnChatPaused.AddListener(SendSQLQuery);
        }
    }

    private void OnDestroy()
    {
        // Unsubscribe from the OnChatPaused event to avoid memory leaks
        if (chatManager != null)
        {
            chatManager.OnChatPaused.RemoveListener(SendSQLQuery);
            Debug.Log("Unsubscribed from OnChatPaused event.");
        }
    }

    public void SendSQLQuery()
    {
        Debug.Log("SendSQLQuery method called.");
        Debug.Log("OnChatPaused event triggered.");
        StartCoroutine(SendRequest());
    }

    private IEnumerator SendRequest()
    {
        Debug.Log("Sending SQL request...");

        // Disable SSL certificate validation (not recommended for production)
        ServicePointManager.ServerCertificateValidationCallback = (sender, certificate, chain, sslPolicyErrors) => true;

        SQLQuery query = new SQLQuery();
        query.sql_query = sqlQuery;

        string json = JsonUtility.ToJson(query);

        UnityWebRequest request = UnityWebRequest.PostWwwForm(serverURL, "POST");
        request.SetRequestHeader("Content-Type", "application/json");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(json);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.ConnectionError)
        {
            Debug.LogError("Network Error: " + request.error);
        }
        else if (request.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("HTTP Error: " + request.responseCode);
        }
        else
        {
            string responseText = request.downloadHandler.text;
            Debug.Log("Success: " + responseText);
        }
    }
}