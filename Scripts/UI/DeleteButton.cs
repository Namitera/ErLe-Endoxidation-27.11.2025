using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DeleteButton : MonoBehaviour
{
    private LogicManagment manager;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
    }

    public void OnButtonPressed()
    {
        manager.deleteButtonPressed = true;
    }
}
