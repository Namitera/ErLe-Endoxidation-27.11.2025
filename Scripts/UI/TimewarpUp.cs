using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimewarpUp : MonoBehaviour
{
    private LogicManagment manager;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
    }

    public void OnButtonPressed()
    {
        manager.increaseTimewarp = true;
    }
}
