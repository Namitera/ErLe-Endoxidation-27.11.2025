using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CameraSnapResetButton : MonoBehaviour
{
    private PlayerCamera playerCamera;

    void Start()
    {
        playerCamera = GameObject.FindGameObjectWithTag("camera1").GetComponent<PlayerCamera>();
    }

    public void OnButtonPressed()
    {
        playerCamera.resetSnap = true;
    }
}
