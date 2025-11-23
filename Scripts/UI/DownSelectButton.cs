using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DownSelectButton : MonoBehaviour
{
    private LogicManagment manager;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
    }

    public void OnButtonPressed()
    {
        manager.selectedParticleIndex -= 1;
    }
}