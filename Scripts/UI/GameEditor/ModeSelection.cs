using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ModeSelection : MonoBehaviour
{
    private Text text;
    private LogicManagment manager;
    public int mode;

    void Start()
    {
        text = GetComponentInChildren<Text>();
        manager = FindAnyObjectByType<LogicManagment>();
        mode = 0;
        text.text = "Game";
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Tab)) UpdateButton(); 
    }

    public void OnButtonPressed()
    {
        UpdateButton();
    }

    void UpdateButton()
    {
        if (text.text == "Game") { text.text = "Editor"; mode = 1; }
        else if (text.text == "Editor") { text.text = "Game"; mode = 0; }
        manager.mode = mode;
    }
}
