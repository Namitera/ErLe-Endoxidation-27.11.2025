using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;


public class MoveTool : MonoBehaviour
{
    private LogicManagment manager;
    private GameEditor editor;
    private Button button;
    private Image image;
    public Image icon1;
    public Image icon2;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        editor = FindAnyObjectByType<GameEditor>();
        image = GetComponent<Image>();
        button = GetComponent<Button>();
    }

    public void OnButtonPressed()
    {
        UpdateButton();
    }

    void Update()
    {
        if (manager.mode == 1)
        {
            button.enabled = true;
            image.enabled = true;
            icon1.enabled = true;
            icon2.enabled = true;
            if (Input.GetKeyDown(KeyCode.T)) UpdateButton(); 
        }
        if (manager.mode != 1)
        {
            button.enabled = false;            
            image.enabled = false;            
            icon1.enabled = false;
            icon2.enabled = false;

        }
        if (editor.selectedTool == 1)
        {
            image.color = new Color32(70,96,124,255);
        }
        else if (editor.selectedTool != 1)
        {
            image.color = new Color(255,255,255);    
        }
    }

    void UpdateButton()
    {
        editor.selectedTool = 1;
        editor.switchedTool = true;
    }
}
