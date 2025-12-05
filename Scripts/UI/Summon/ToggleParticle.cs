using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleParticle : MonoBehaviour
{
    private LogicManagment manager;
    private Text text;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        text = GetComponentInChildren<Text>();
    }

    public void OnButtonPressed()
    {
        manager.toggleParticleState = !manager.toggleParticleState;
        if (manager.toggleParticleState) text.text = "on";
        if (!manager.toggleParticleState) text.text = "off";
    }
}