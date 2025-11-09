using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCamera : MonoBehaviour
{

    public Camera playercam;
    public float speed = 1;
    public float zoomSpeed = 0.1f;

    
    void Start()
    {
        playercam = GetComponent<Camera>();
    }

    void Update()
    {
        if (Input.GetKey(KeyCode.W)) playercam.transform.position += Vector3.up * speed;        
        if (Input.GetKey(KeyCode.S)) playercam.transform.position += Vector3.down * speed;        
        if (Input.GetKey(KeyCode.A)) playercam.transform.position += Vector3.left * speed;        
        if (Input.GetKey(KeyCode.D)) playercam.transform.position += Vector3.right * speed;        
        if (Input.GetKey(KeyCode.E)) playercam.orthographicSize -= zoomSpeed;
        if (Input.GetKey(KeyCode.Q)) playercam.orthographicSize += zoomSpeed;
        if (playercam.orthographicSize < 0.1) playercam.orthographicSize = 0.1f;    
    }
}
