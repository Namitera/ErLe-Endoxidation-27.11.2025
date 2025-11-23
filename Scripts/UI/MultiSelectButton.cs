using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MultiSelectButton : MonoBehaviour
{
    private LogicManagment manager;
    private Text text;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        text = GetComponentInChildren<Text>();
        text.text = "1";
        manager.particleCountButton = 1;
    }

    public void OnButtonPressed()
    {
        if (manager.particleCountButton == 1)
        {
            manager.particleCountButton = 10;
            text.text = "10";
        } else if (manager.particleCountButton == 10)
        {
            manager.particleCountButton = 100;
            text.text = "100";
        } else if (manager.particleCountButton == 100)
        {
            manager.particleCountButton = 1;
            text.text = "1";
        }
    }
}
