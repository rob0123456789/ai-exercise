# Copy/paste this code snippet beneath the 'bounding box' section':
# Mind the indentations!!

    # Define a "blur" over the face
    if state =='blur':
        kernel_width = (w // 7) | 1
        kernel_height = (h // 7) | 1

        for i in range(0, output.shape[0]):
            confidence = output[i, 2]
            # get the confidence
            # if confidence is above 40%, then blur the bounding box (face)
            if confidence > 0.4:
                # get the surrounding box cordinates and upscale them to original image
                box = output[i, 3:7] * np.array([w, h, w, h])
                # convert to integers
                start_x, start_y, end_x, end_y = box.astype(np.int64)
                # get the face image
                face = image[start_y: end_y, start_x: end_x]
                # apply gaussian blur to this face
                face = cv2.GaussianBlur(face, (kernel_width, kernel_height), 0)
                # put the blurred face into the original image
                image[start_y: end_y, start_x: end_x] = face