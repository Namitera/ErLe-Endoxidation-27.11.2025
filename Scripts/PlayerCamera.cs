using UnityEngine;

public class PlayerCamera : MonoBehaviour
{

    public Camera playercam;
    public float speed = 1;
    public float zoomSpeed = 0.05f;
    private GameObject targetObject;
    public bool snapCamera;
    public bool resetSnap;

    
    void Start()
    {
        playercam = GetComponent<Camera>();
        targetObject = null;
        snapCamera = false;
    }

    void Update()
    {
        KeyboardMovement();

        TouchMovement();
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
        if (Input.GetKey(KeyCode.W)) playercam.transform.position += Vector3.up * speed;        
        if (Input.GetKey(KeyCode.S)) playercam.transform.position += Vector3.down * speed;        
        if (Input.GetKey(KeyCode.A)) playercam.transform.position += Vector3.left * speed;        
        if (Input.GetKey(KeyCode.D)) playercam.transform.position += Vector3.right * speed;        
        if (Input.GetKey(KeyCode.E)) playercam.orthographicSize -= zoomSpeed * playercam.orthographicSize;
        if (Input.GetKey(KeyCode.Q)) playercam.orthographicSize += zoomSpeed * playercam.orthographicSize;
        if (playercam.orthographicSize < 0.5) playercam.orthographicSize = 0.5f;    
        if (playercam.orthographicSize > 1000) playercam.orthographicSize = 1000f;    

        if (Input.GetKeyDown(KeyCode.Mouse0) && snapCamera)
        {
            Vector2 mousePos = playercam.ScreenToWorldPoint(Input.mousePosition);
            RaycastHit2D hit = Physics2D.Raycast(mousePos, new Vector2(0, 0), 1000000, -1);
            if (hit.collider != null) targetObject = hit.collider.gameObject;
        }
        if (Input.GetKeyDown(KeyCode.Mouse1) && !Input.GetKey(KeyCode.Mouse0)) targetObject = null;

        if (resetSnap)
        {
            resetSnap = false;
            targetObject = null;
        }
        if (targetObject != null) transform.position = new Vector3(targetObject.transform.position.x, targetObject.transform.position.y, transform.position.z);
    }
}
