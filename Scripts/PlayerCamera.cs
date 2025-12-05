using Unity.Burst.Intrinsics;
using UnityEngine;
using UnityEngine.EventSystems;

public class PlayerCamera : MonoBehaviour
{
    public Camera playercam;
    public float acceleration = 1;
    public float friction = 0.9f;
    public float zoomAcceleration = 0.05f;
    public float maxDistance = 2000;
    public float zoomSpeed;
    public float zoomFriction;

    [SerializeField]
    private GameObject targetObject;
    public bool snapCamera;
    public bool resetSnap;
    private float speedX;
    private float speedY;
    private LogicManagment manager;
    private GameEditor editor;

    
    void Start()
    {
        playercam = GetComponent<Camera>();
        manager = FindAnyObjectByType<LogicManagment>();
        editor = FindAnyObjectByType<GameEditor>();
        targetObject = null;
        snapCamera = true;
    }

    void Update()
    {
        KeyboardMovement();

        Snapping();

        if (editor.hasTargetObject == false) TouchMovement();

        MaxDistance();
    }

    void MaxDistance()
    {
        Vector2 pos = new Vector2(transform.position.x, transform.position.y);
        Vector3 zPos = new Vector3(0,0,transform.position.z);
        if (pos.magnitude > maxDistance) transform.position = new Vector3(pos.x, pos.y, 0).normalized * maxDistance + zPos;
    }

    void TouchMovement()
    {
        // touch control
        if (Input.touchCount == 1)
        {
            Touch firstTouch = Input.GetTouch(0);
            if (firstTouch.phase == TouchPhase.Moved)
            {
                Vector3 pos = playercam.ScreenToWorldPoint(firstTouch.position);
                Vector3 oldPos = playercam.ScreenToWorldPoint(firstTouch.position - firstTouch.deltaPosition);
                Vector3 deltaPos = oldPos - pos;
                transform.position += deltaPos;
            }
        } 

        if (Input.touchCount == 2)
        {
            Touch firstTouch = Input.GetTouch(0);
            Touch secondTouch = Input.GetTouch(1);

            if (firstTouch.phase == TouchPhase.Moved || secondTouch.phase == TouchPhase.Moved)
            {
                Vector3 newPos1 = playercam.ScreenToWorldPoint(firstTouch.position);
                Vector3 newPos2 = playercam.ScreenToWorldPoint(secondTouch.position);

                Vector3 oldPos1 = playercam.ScreenToWorldPoint(firstTouch.position - firstTouch.deltaPosition);
                Vector3 oldPos2 = playercam.ScreenToWorldPoint(secondTouch.position - secondTouch.deltaPosition);

                Vector3 newDistance = newPos2 - newPos1;
                Vector3 oldDistance = oldPos2 - oldPos1;

                Vector3 deltaDistance = newDistance - oldDistance;

                float zoomDirection = 1;
                if (newDistance.sqrMagnitude > oldDistance.sqrMagnitude) zoomDirection = -1; 
                if (newDistance.sqrMagnitude <= oldDistance.sqrMagnitude) zoomDirection = 1; 

                playercam.orthographicSize += zoomDirection * deltaDistance.magnitude;
                if (playercam.orthographicSize < 0.5) playercam.orthographicSize = 0.5f;    
                if (playercam.orthographicSize > 1000) playercam.orthographicSize = 1000f; 
            }
        }
    }


    void KeyboardMovement()
    {
        if (Input.GetKey(KeyCode.W)) speedY += 1 * acceleration *(playercam.orthographicSize/1000);        
        if (Input.GetKey(KeyCode.S)) speedY += -1 * acceleration *(playercam.orthographicSize/1000);        
        if (Input.GetKey(KeyCode.D)) speedX += 1 * acceleration *(playercam.orthographicSize/1000);        
        if (Input.GetKey(KeyCode.A)) speedX += -1 * acceleration *(playercam.orthographicSize/1000);        

        speedX *= friction;
        speedY *= friction;

        playercam.transform.position += new Vector3(speedX, speedY, 0);

        if (Input.GetKey(KeyCode.E)) zoomSpeed -= zoomAcceleration * playercam.orthographicSize;
        if (Input.GetKey(KeyCode.Q)) zoomSpeed += zoomAcceleration * playercam.orthographicSize;

        zoomSpeed *= zoomFriction;

        playercam.orthographicSize += zoomSpeed;

        if (playercam.orthographicSize < 0.5) playercam.orthographicSize = 0.5f;    
        if (playercam.orthographicSize > 1000) playercam.orthographicSize = 1000f;    
    }

    void Snapping()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0) && snapCamera)
        {
            Vector2 mousePos = playercam.ScreenToWorldPoint(Input.mousePosition);
            if (EventSystem.current.IsPointerOverGameObject()) return;
            if (Input.touchCount > 0) if (EventSystem.current.IsPointerOverGameObject(Input.GetTouch(0).fingerId)) return;
            RaycastHit2D hit = Physics2D.Raycast(mousePos, new Vector2(0, 0), 1000000, -1);
            if (hit.collider != null) targetObject = hit.collider.gameObject;
        }
        if (Input.GetKeyDown(KeyCode.Mouse1) && !Input.GetKey(KeyCode.Mouse0)) targetObject = null;

        if (manager.mode != 0) resetSnap = true;
        if (resetSnap)
        {
            resetSnap = false;
            targetObject = null;
        }
        if (targetObject != null) transform.position = new Vector3(targetObject.transform.position.x, targetObject.transform.position.y, transform.position.z);
    }
}
