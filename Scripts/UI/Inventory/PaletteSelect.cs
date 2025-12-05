using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PaletteSelect : MonoBehaviour
{
    private InventoryManager manager;
    private Text text;

    void Start()
    {
        manager = FindAnyObjectByType<InventoryManager>();
        text = GetComponentInChildren<Text>();
        text.text = "1";
        manager.palette = 1;
    }

    public void OnButtonPressed()
    {
        if (manager.palette == 1)
        {
            manager.palette = 2;
            text.text = "2";
        } else if (manager.palette == 2)
        {
            manager.palette = 3;
            text.text = "3";
        } else if (manager.palette == 3)
        {
            manager.palette = 1;
            text.text = "1";
        }
    }
}
