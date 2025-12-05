using System;
using cakeslice;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.EventSystems;

public class GameEditor : MonoBehaviour
{
    private LogicManagment manager;
    private Camera playerCam;
    public int selectedTool;
    public bool switchedTool;

    private bool activateMito;
    public GameObject c1;
    public GameObject c2;
    public GameObject c3;
    public GameObject c4;
    public GameObject c5;
    public GameObject mito;

    public GameObject protein1;
    public GameObject protein2;
    public GameObject protein3;
    public GameObject protein4;
    public GameObject protein5;

    public GameObject membrane1;
    public GameObject membrane2;
    public GameObject membrane3;
    public GameObject membraneBow1;
    public GameObject membraneBow2;
    public GameObject membraneBow3;
    public GameObject membraneBowSharp1;
    public GameObject membraneBowSharp2;
    public GameObject membraneBowSharp3;
    private GameObject targetObject;
    public bool hasTargetObject;
    private float angleInit;
    private float targetObjectAngle;
    private DeleteTool deleteTool;
    private GameObject summonUI;
    private InventoryManager inventoryManager;
    


    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        deleteTool = FindAnyObjectByType<DeleteTool>();
        inventoryManager = FindAnyObjectByType<InventoryManager>();
        playerCam = GameObject.FindGameObjectWithTag("camera1").GetComponent<Camera>();
        summonUI = GameObject.FindGameObjectWithTag("summonui");
        targetObject = null;
        angleInit = 0;
        targetObjectAngle = 0;
        selectedTool = 0;
        switchedTool = false;

        mito.SetActive(false);
    }

    void Update()
    {
        if (manager.mode == 0)
        {
            if (Input.GetKeyDown(KeyCode.Alpha6)) activateMito = !activateMito;  
            mito.SetActive(activateMito);  
            summonUI.SetActive(true);
        }
        if (manager.mode == 1)
        {
            summonUI.SetActive(false);
            EditorMode();
        }
        if (manager.mode != 1)
        {
            ResetEditorMode();
            selectedTool = 0;
        }
    }

    void EditorMode()
    {
        if (switchedTool) { ResetEditorMode(); switchedTool = false; }
        DeleteTool();
        if (selectedTool == 1) MoveTool();
        if (selectedTool == 2) RotateTool();
        PlaceObjects();
        if (targetObject != null) hasTargetObject = true;
        if (targetObject == null) hasTargetObject = false;
    }

    void ResetEditorMode()
    {
        if (targetObject != null)
        {
            targetObject.GetComponent<Outline>().enabled = false;
            targetObject = null;   
        }   
    }

    void MoveTool()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            Vector2 mousePos = playerCam.ScreenToWorldPoint(Input.mousePosition);
            if (EventSystem.current.IsPointerOverGameObject()) return;
            if (Input.touchCount > 0) if (EventSystem.current.IsPointerOverGameObject(Input.GetTouch(0).fingerId)) return;
            RaycastHit2D hit = Physics2D.Raycast(mousePos, new Vector2(0, 0), 1000000, 1 << 9);
            if (hit.collider != null) targetObject = hit.collider.gameObject.transform.root.gameObject;

            if (targetObject != null && targetObject.GetComponent<Outline>() == null) targetObject = null;
            if (targetObject != null && targetObject.GetComponent<Outline>() != null)
            {
                targetObject.GetComponent<Outline>().enabled = true;
            }
        }

        if (targetObject != null)
        {
            Vector2 mousePos = playerCam.ScreenToWorldPoint(Input.mousePosition);
            targetObject.transform.position = mousePos;

            if (Input.GetKeyUp(KeyCode.Mouse0))
            {
                targetObject.GetComponent<Outline>().enabled = false;
                targetObject = null;   
            }
        } 
    }

    void RotateTool()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            Vector2 mousePos = playerCam.ScreenToWorldPoint(Input.mousePosition);
            if (EventSystem.current.IsPointerOverGameObject()) return;
            if (Input.touchCount > 0) if (EventSystem.current.IsPointerOverGameObject(Input.GetTouch(0).fingerId)) return;
            RaycastHit2D hit = Physics2D.Raycast(mousePos, new Vector2(0, 0), 1000000, 1 << 9);
            if (hit.collider != null) targetObject = hit.collider.gameObject.transform.root.gameObject;

            if (targetObject != null && targetObject.GetComponent<Outline>() == null) targetObject = null;
            if (targetObject != null && targetObject.GetComponent<Outline>() != null)
            {
                targetObject.GetComponent<Outline>().enabled = true;
                Vector2 targetPos = new Vector2(targetObject.transform.position.x, targetObject.transform.position.y);
                angleInit = Mathf.Atan2(mousePos.y - targetPos.y, mousePos.x - targetPos.x) * Mathf.Rad2Deg;
                targetObjectAngle = targetObject.transform.eulerAngles.z;
            }
        }

        if (targetObject != null)
        {
            Vector2 mousePos = playerCam.ScreenToWorldPoint(Input.mousePosition);
            Vector2 targetPos = new Vector2(targetObject.transform.position.x, targetObject.transform.position.y);

            float angle = Mathf.Atan2(mousePos.y - targetPos.y, mousePos.x - targetPos.x) * Mathf.Rad2Deg;
            targetObject.transform.rotation = Quaternion.Euler(0,0,targetObjectAngle + angle - angleInit);

            if (Input.GetKeyUp(KeyCode.Mouse0))
            {
                targetObject.GetComponent<Outline>().enabled = false;
                targetObject = null;   
            }
        } 
    }

    void DeleteTool()
    {
        UnityEngine.UI.Image image = deleteTool.image;
        if (targetObject != null)
        {
            image.color = new Color32(70,96,124,255);
            RectTransform deleteRect = deleteTool.rectTransform;

            if (!RectTransformUtility.RectangleContainsScreenPoint(deleteRect, Input.mousePosition, playerCam)) return;
            image.color = new Color32(255,0,0,255);
            if (!Input.GetKeyUp(KeyCode.Mouse0)) return;
            Destroy(targetObject.gameObject);
        }
        else
        {
            image.color = new Color(255,255,255);        
        }
    }

    void PlaceObjects()
    {
        int toPlaceObject = -1;
        if (inventoryManager.canPlace || Input.GetKeyDown(KeyCode.Space))
        {
            inventoryManager.canPlace = false;
            if (inventoryManager.palette == 1)
            {
                if (inventoryManager.selectedSlot == 0) toPlaceObject = 1;
                if (inventoryManager.selectedSlot == 1) toPlaceObject = 2;
                if (inventoryManager.selectedSlot == 2) toPlaceObject = 3;
                if (inventoryManager.selectedSlot == 3) toPlaceObject = 4;
                if (inventoryManager.selectedSlot == 4) toPlaceObject = 5;
            }
            if (inventoryManager.palette == 2)
            {
                if (inventoryManager.selectedSlot == 0) toPlaceObject = 11;
                if (inventoryManager.selectedSlot == 1) toPlaceObject = 12;
                if (inventoryManager.selectedSlot == 2) toPlaceObject = 13;
                if (inventoryManager.selectedSlot == 3) toPlaceObject = 14;
                if (inventoryManager.selectedSlot == 4) toPlaceObject = 15;
            }
            if (inventoryManager.palette == 3)
            {
                if (inventoryManager.selectedSlot == 0) toPlaceObject = 21;
                if (inventoryManager.selectedSlot == 1) toPlaceObject = 22;
                if (inventoryManager.selectedSlot == 2) toPlaceObject = 23;
                if (inventoryManager.selectedSlot == 3) toPlaceObject = 24;
                if (inventoryManager.selectedSlot == 4) toPlaceObject = 25;
                if (inventoryManager.selectedSlot == 5) toPlaceObject = 26;
                if (inventoryManager.selectedSlot == 6) toPlaceObject = 27;
                if (inventoryManager.selectedSlot == 7) toPlaceObject = 28;
                if (inventoryManager.selectedSlot == 8) toPlaceObject = 29;
            }
        }
        if (Input.anyKeyDown)
        {
            if (Input.GetKeyDown(KeyCode.C)) {toPlaceObject = 1;}
            if (Input.GetKeyDown(KeyCode.V)) {toPlaceObject = 2;}
            if (Input.GetKeyDown(KeyCode.B)) {toPlaceObject = 3;}
            if (Input.GetKeyDown(KeyCode.N)) {toPlaceObject = 4;}
            if (Input.GetKeyDown(KeyCode.M)) {toPlaceObject = 5;}

            if (Input.GetKeyDown(KeyCode.F)) {toPlaceObject = 11;}
            if (Input.GetKeyDown(KeyCode.G)) {toPlaceObject = 12;}
            if (Input.GetKeyDown(KeyCode.H)) {toPlaceObject = 13;}
            if (Input.GetKeyDown(KeyCode.J)) {toPlaceObject = 14;}
            if (Input.GetKeyDown(KeyCode.K)) {toPlaceObject = 15;}

            if (Input.GetKeyDown(KeyCode.Alpha1)) {toPlaceObject = 21;}
            if (Input.GetKeyDown(KeyCode.Alpha2)) {toPlaceObject = 22;}
            if (Input.GetKeyDown(KeyCode.Alpha3)) {toPlaceObject = 23;}
            if (Input.GetKeyDown(KeyCode.Alpha4)) {toPlaceObject = 24;}
            if (Input.GetKeyDown(KeyCode.Alpha5)) {toPlaceObject = 25;}
            if (Input.GetKeyDown(KeyCode.Alpha6)) {toPlaceObject = 26;}
            if (Input.GetKeyDown(KeyCode.Alpha7)) {toPlaceObject = 27;}
            if (Input.GetKeyDown(KeyCode.Alpha8)) {toPlaceObject = 28;}
            if (Input.GetKeyDown(KeyCode.Alpha9)) {toPlaceObject = 29;}
        }

        if (toPlaceObject == -1) return;
        Vector3 camPos = playerCam.transform.position - new Vector3(0,0, playerCam.transform.position.z);

        switch (toPlaceObject)
        {
            case 1: Instantiate(protein1, camPos, Quaternion.identity); break;
            case 2: Instantiate(protein2, camPos, Quaternion.identity); break;
            case 3: Instantiate(protein3, camPos, Quaternion.identity); break;
            case 4: Instantiate(protein4, camPos, Quaternion.identity); break;
            case 5: Instantiate(protein5, camPos, Quaternion.identity); break;

            case 11: Instantiate(c1, camPos, Quaternion.identity); break;
            case 12: Instantiate(c2, camPos, Quaternion.identity); break;
            case 13: Instantiate(c3, camPos, Quaternion.identity); break;
            case 14: Instantiate(c4, camPos, Quaternion.identity); break;
            case 15: Instantiate(c5, camPos, Quaternion.identity); break;

            case 21: Instantiate(membrane1, camPos, Quaternion.identity); break;
            case 22: Instantiate(membrane2, camPos, Quaternion.identity); break;
            case 23: Instantiate(membrane3, camPos, Quaternion.identity); break;
            case 24: Instantiate(membraneBow1, camPos, Quaternion.identity); break;
            case 25: Instantiate(membraneBow2, camPos, Quaternion.identity); break;
            case 26: Instantiate(membraneBow3, camPos, Quaternion.identity); break;
            case 27: Instantiate(membraneBowSharp1, camPos, Quaternion.identity); break;
            case 28: Instantiate(membraneBowSharp2, camPos, Quaternion.identity); break;
            case 29: Instantiate(membraneBowSharp3, camPos, Quaternion.identity); break;
        }
    }
}
