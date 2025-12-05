using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RotateTool : MonoBehaviour
{
    private LogicManagment manager;
    private GameEditor editor;
    private Button button;
    private Image image;
    public Image icon;


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
            icon.enabled = true;
            if (Input.GetKeyDown(KeyCode.R)) UpdateButton(); 
        }
        if (manager.mode != 1)
        {
            button.enabled = false;            
            image.enabled = false;            
            icon.enabled = false;
        }
        if (editor.selectedTool == 2)
        {
            image.color = new Color32(70,96,124,255);
        }
        else if (editor.selectedTool != 2)
        {
            image.color = new Color(255,255,255);    
        }
    }

    void UpdateButton()
    {
        editor.selectedTool = 2;
        editor.switchedTool = true;
    }
}
