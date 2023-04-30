# Copy/paste this code snippet beneath the line:
# output = np.squeeze(model.forward())
# Mind the indentations!!

    # Define a "bounding box" around the face
    if state == 'box':
        for i in range(0, output.shape[0]):
            # get the confidence
            confidence = output[i, 2]
            # if confidence is above 45%, then draw the surrounding box
            if confidence > 0.45:
                # get the surrounding box cordinates and upscale them to original image
                box = output[i, 3:7] * np.array([w, h, w, h])
                # convert to integers
                start_x, start_y, end_x, end_y = box.astype(np.int64)
                # draw the rectangle surrounding the face
                cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
                # draw text as well
                cv2.putText(image, f"{confidence*100:.2f}%", (start_x, start_y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
