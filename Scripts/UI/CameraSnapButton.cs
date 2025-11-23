using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CameraSnapButton : MonoBehaviour
{
    private PlayerCamera playerCamera;
    private Text text;

    void Start()
    {
        playerCamera = GameObject.FindGameObjectWithTag("camera1").GetComponent<PlayerCamera>();
        text = GetComponentInChildren<Text>();
    }

    public void OnButtonPressed()
    {
        playerCamera.snapCamera = !playerCamera.snapCamera;
        if (playerCamera.snapCamera) text.text = "on";
        if (!playerCamera.snapCamera) text.text = "off";
    }
}
