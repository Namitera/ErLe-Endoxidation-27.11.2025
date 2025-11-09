using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEngine;
using UnityEngine.AI;

public class LogicManagment : MonoBehaviour
{
    public GameObject particle;
    public GameObject nad;
    public GameObject fad;
    public Camera playercam;
    private Vector3 spawnPosition;

    void Start()
    {
        playercam = GameObject.FindGameObjectWithTag("camera1").GetComponent<Camera>();
    }

    void Update()
    {
        spawnPosition = new Vector3(playercam.transform.position.x, playercam.transform.position.y, 0);

        SpawnKeys();

        if (Input.GetKeyDown(KeyCode.R))
        {
            NAD[] nads = FindObjectsOfType<NAD>();
            Proton[] protons = FindObjectsOfType<Proton>();
            FADBase[] fads = FindObjectsOfType<FADBase>();

            foreach (NAD nad in nads) { Destroy(nad.gameObject); }
            foreach (Proton proton in protons) { Destroy(proton.gameObject); }
            foreach (FADBase fad in fads) { Destroy(fad.gameObject); }
        }
    }


    void SpawnKeys()
    {
        if (Input.GetKeyDown(KeyCode.Space)) Instantiate(particle, spawnPosition, Quaternion.identity);
        if (Input.GetKeyDown(KeyCode.T))
        {
            for (int i = 1; i <= 10; i++)
            {
                Instantiate(particle, spawnPosition, Quaternion.identity);
            }
        }
        if (Input.GetKeyDown(KeyCode.H))
        {
            for (int i = 1; i <= 100; i++)
            {
                Instantiate(particle, spawnPosition, Quaternion.identity);
            }
        }

        if (Input.GetKeyDown(KeyCode.X)) Instantiate(nad, spawnPosition, Quaternion.identity);
        if (Input.GetKeyDown(KeyCode.C))
        {
            for (int i = 1; i <= 10; i++)
            {
                Instantiate(nad, spawnPosition, Quaternion.identity);
            }
        }
        if (Input.GetKeyDown(KeyCode.V))
        {
            for (int i = 1; i <= 100; i++)
            {
                Instantiate(nad, spawnPosition, Quaternion.identity);
            }
        }


        if (Input.GetKeyDown(KeyCode.B)) Instantiate(fad, spawnPosition, Quaternion.identity);
        if (Input.GetKeyDown(KeyCode.N))
        {
            for (int i = 1; i <= 10; i++)
            {
                Instantiate(fad, spawnPosition, Quaternion.identity);
            }
        }
        if (Input.GetKeyDown(KeyCode.M))
        {
            for (int i = 1; i <= 100; i++)
            {
                Instantiate(fad, spawnPosition, Quaternion.identity);
            }
        }
    }
}
