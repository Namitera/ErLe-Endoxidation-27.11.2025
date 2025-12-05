using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEditor;
using UnityEngine;

public class LogicManagment : MonoBehaviour
{
    public GameObject particle;
    public GameObject nad;
    public GameObject fadh2;
    public GameObject electron;
    public GameObject ubiquinone;
    public GameObject cytochromec;
    public GameObject oxygen;
    public GameObject adp;
    public GameObject phosphorus;
    public GameObject hydrogen;
    public GameObject nadplus;
    public GameObject fad;
    public GameObject qh2;
    public GameObject cytcred;
    public GameObject h2o;
    public GameObject atp;

    public GameObject toSpawnParticle;

    public Camera playercam;
    private Vector3 spawnPosition;
    public float brownianMotionMultiplier = 1;
    public bool increaseTimewarp;
    public bool decreaseTimewarp;
    private bool isShifting;
    private bool isCtrl;
    private bool isToggling;

    // UI
    public bool spawnButtonPressed;
    public bool deleteButtonPressed;
    public int selectedParticleIndex;
    public bool toggleParticleState;
    public int particleCountButton;
    public int mode;

    
    void OnPreRender()
    {
        GL.Clear(true, true, Color.black);
    }

    void Start()
    {
        playercam = GameObject.FindGameObjectWithTag("camera1").GetComponent<Camera>();
        increaseTimewarp = false;
        decreaseTimewarp = false;
        Time.timeScale = 1;
        isShifting = false;
        isCtrl = false;
        isToggling = false;

        spawnButtonPressed = false;
        deleteButtonPressed = false;
        selectedParticleIndex = 0;
        toggleParticleState = false;

        toSpawnParticle = null;
        GetParticleObject();
    }


    void Update()
    {
        if (mode == 0)
        {
            SpawnKeys();
            if (spawnButtonPressed) SpawnButton();    
            ResetParticles();
        }
        if (mode == 1)
        {
            if (spawnButtonPressed) spawnButtonPressed = false;
        }

        GetParticleObject(); // so that ui works runtime
        Timewarp();
    }


    void ResetParticles()
    {
        if (Input.GetKeyDown(KeyCode.R) || deleteButtonPressed)
        {
            deleteButtonPressed = false;

            NAD[] nads = FindObjectsOfType<NAD>();
            Proton[] protons = FindObjectsOfType<Proton>();
            FADBase[] fads = FindObjectsOfType<FADBase>();
            Electron[] electrons = FindObjectsOfType<Electron>();
            Ubiquinone[] ubiquinones = FindObjectsOfType<Ubiquinone>();
            CytochromeC[] cytochromeCs = FindObjectsOfType<CytochromeC>();
            Oxygen[] oxygens = FindObjectsOfType<Oxygen>();
            Phosphorus[] phosphoruss = FindObjectsOfType<Phosphorus>();
            ADP[] adps = FindObjectsOfType<ADP>();


            foreach (NAD nad in nads) { Destroy(nad.gameObject); }
            foreach (Proton proton in protons) { Destroy(proton.gameObject); }
            foreach (FADBase fadh2 in fads) { Destroy(fadh2.gameObject); }
            foreach (Electron electron in electrons) { Destroy(electron.gameObject); }
            foreach (Ubiquinone ubiquinone in ubiquinones) { Destroy(ubiquinone.gameObject); }
            foreach (CytochromeC cytochromeC in cytochromeCs) { Destroy(cytochromeC.gameObject); }
            foreach (Oxygen oxygen in oxygens) { Destroy(oxygen.gameObject); }
            foreach (Phosphorus phosphorus in phosphoruss) { Destroy(phosphorus.gameObject); }
            foreach (ADP adp in adps) { Destroy(adp.gameObject); }
        }   
    }


    void Timewarp()
    {
        if (Input.GetKeyDown(KeyCode.Period)) increaseTimewarp = true;
        if (Input.GetKeyDown(KeyCode.Comma)) decreaseTimewarp = true;
        int maxTimewarp = 5;
        if (increaseTimewarp)
        {
            Time.timeScale += 1;
            increaseTimewarp = false;
        }
        if (decreaseTimewarp)
        {
            if (Time.timeScale > 0) Time.timeScale -= 1;
            decreaseTimewarp = false;
        }
        if (Time.timeScale > maxTimewarp) Time.timeScale = maxTimewarp;
    }

    void SpawnButton()
    {
        spawnButtonPressed = false;
        int particleCount = particleCountButton;
        spawnPosition = new Vector3(playercam.transform.position.x, playercam.transform.position.y, 0);

        GetParticleObject();

        if (toSpawnParticle == null) return; 

        for (int i = 1; i <= particleCount; i++)
        {
            Instantiate(toSpawnParticle, spawnPosition, Quaternion.identity);
        }
    }

    void GetParticleObject()
    {
        if (selectedParticleIndex < 0) selectedParticleIndex = 0;
        if (selectedParticleIndex > 8) selectedParticleIndex = 8;

        if (selectedParticleIndex == 3) toSpawnParticle = electron;
        if (selectedParticleIndex == 7) toSpawnParticle = phosphorus;

        if (!toggleParticleState)
        {
            if (selectedParticleIndex == 0) toSpawnParticle = particle;
            if (selectedParticleIndex == 1) toSpawnParticle = nad;
            if (selectedParticleIndex == 2) toSpawnParticle = fadh2;
            if (selectedParticleIndex == 4) toSpawnParticle = ubiquinone;
            if (selectedParticleIndex == 5) toSpawnParticle = cytochromec;
            if (selectedParticleIndex == 6) toSpawnParticle = oxygen;
            if (selectedParticleIndex == 8) toSpawnParticle = adp;            
        }
        if (toggleParticleState)
        {
            if (selectedParticleIndex == 0) toSpawnParticle = hydrogen;
            if (selectedParticleIndex == 1) toSpawnParticle = nadplus;
            if (selectedParticleIndex == 2) toSpawnParticle = fad;
            if (selectedParticleIndex == 4) toSpawnParticle = qh2;
            if (selectedParticleIndex == 5) toSpawnParticle = cytcred;
            if (selectedParticleIndex == 6) toSpawnParticle = h2o;
            if (selectedParticleIndex == 8) toSpawnParticle = atp;   
        }   
    }

    void SpawnKeys()
    {
        int particleCount = 1;
        GameObject toSpawnParticle = null;
        spawnPosition = new Vector3(playercam.transform.position.x, playercam.transform.position.y, 0);

        if (Input.GetKey(KeyCode.LeftShift)) isShifting = true;
        if (Input.GetKeyUp(KeyCode.LeftShift)) isShifting = false;
        if (Input.GetKey(KeyCode.LeftControl)) isCtrl = true;
        if (Input.GetKeyUp(KeyCode.LeftControl)) isCtrl = false;
        if (Input.GetKey(KeyCode.LeftAlt)) isToggling = true;
        if (Input.GetKeyUp(KeyCode.LeftAlt)) isToggling = false;

        if (isShifting) particleCount = 10;
        if (isCtrl) particleCount = 100;

        if (Input.GetKeyDown(KeyCode.T)) toSpawnParticle = phosphorus;
        if (Input.GetKeyDown(KeyCode.C)) toSpawnParticle = electron;

        if (!isToggling)
        {
            if (Input.GetKeyDown(KeyCode.Space)) toSpawnParticle = particle;
            if (Input.GetKeyDown(KeyCode.Y)) toSpawnParticle = nad;
            if (Input.GetKeyDown(KeyCode.X)) toSpawnParticle = fadh2;
            if (Input.GetKeyDown(KeyCode.V)) toSpawnParticle = ubiquinone;
            if (Input.GetKeyDown(KeyCode.F)) toSpawnParticle = cytochromec;
            if (Input.GetKeyDown(KeyCode.G)) toSpawnParticle = oxygen;
            if (Input.GetKeyDown(KeyCode.L)) toSpawnParticle = adp;            
        }
        if (isToggling)
        {
            if (Input.GetKeyDown(KeyCode.Space)) toSpawnParticle = hydrogen;
            if (Input.GetKeyDown(KeyCode.Y)) toSpawnParticle = nadplus;
            if (Input.GetKeyDown(KeyCode.X)) toSpawnParticle = fad;
            if (Input.GetKeyDown(KeyCode.V)) toSpawnParticle = qh2;
            if (Input.GetKeyDown(KeyCode.F)) toSpawnParticle = cytcred;
            if (Input.GetKeyDown(KeyCode.G)) toSpawnParticle = h2o;
            if (Input.GetKeyDown(KeyCode.L)) toSpawnParticle = atp;            
        }

        if (toSpawnParticle == null) return; 

        for (int i = 1; i <= particleCount; i++)
        {
            Instantiate(toSpawnParticle, spawnPosition, Quaternion.identity);
        }
    }
}
