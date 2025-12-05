using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DeleteTool : MonoBehaviour
{
    private LogicManagment manager;
    private Button button;
    public Image image;
    public Image icon1;
    public RectTransform rectTransform;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        image = GetComponent<Image>();
        button = GetComponent<Button>();
        rectTransform = GetComponent<RectTransform>();
    }

    void Update()
    {
        if (manager.mode == 1)
        {
            button.enabled = true;
            image.enabled = true;
            icon1.enabled = true;
        }
        if (manager.mode != 1)
        {
            button.enabled = false;            
            image.enabled = false;            
            icon1.enabled = false;
        }
    }
}
