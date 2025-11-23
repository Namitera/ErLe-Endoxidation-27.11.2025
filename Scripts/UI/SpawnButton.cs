using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class SpawnButton : MonoBehaviour
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
        manager.spawnButtonPressed = true;
    }

    void Update()
    {
        text.text = "Spawn" + manager.selectedParticleIndex;
    }
}
