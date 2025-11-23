using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimewarpDown : MonoBehaviour
{
    private LogicManagment manager;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
    }

    public void OnButtonPressed()
    {
        manager.decreaseTimewarp = true;
    }
}
