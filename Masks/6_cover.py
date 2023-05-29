# Paste this snippet after the section for 'blur'

                
    # replace the face with another face
    if state == 'cover':
        cover_im = cv2.imread(file_path + '\\Test_images\\smileyface.jpg')
        for i in range(0, output.shape[0]):
            confidence = output[i, 2]
            # get the confidence
            # if confidence is above 40%, then blur the bounding box (face)
            if confidence > 0.4:
                # get the surrounding box cordinates and upscale them to original image
                box = output[i, 3:7] * np.array([w, h, w, h])
                # convert to integers
                start_x, start_y, end_x, end_y = box.astype(np.int64)
                w = end_x - start_x
                h = end_y - start_y
                dim = (w,h)
                cover_im = cv2.resize(cover_im, dim)
                # get the face image
                face = cover_im
                # apply gaussian blur to this face
                # put the blurred face into the original image
                image[start_y: end_y, start_x: end_x] = face
