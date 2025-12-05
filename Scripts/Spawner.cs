using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public float frequency = 1;
    public int amount = 1;
    public int spawnLimit = 100;
    public GameObject spawnObject;
    private float time;
    private bool canSpawn;
    [SerializeField]
    private int spawnedObjects;

    void Awake()
    {
        canSpawn = false;
        spawnedObjects = 0;
    }

    void FixedUpdate()
    {
        time = Time.fixedTime;
        this.name = "Spawner" + " (" + spawnObject.name + ")";

        if (canSpawn && time % frequency < (0.5 * frequency))
        {
            canSpawn = false;
            if (spawnObject == null) return;
            for (int i = 1; i <= amount; i++)
            {
                Instantiate(spawnObject, transform.position, Quaternion.identity);
                spawnedObjects += 1;
            }
        }

        if (spawnedObjects < spawnLimit && time % frequency > (0.5 * frequency))
        {
            canSpawn = true;
        }
    }
}
