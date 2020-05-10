import pygame

def set_ships(ship_list,keys):
    if len(ship_list) <= 30:
        if keys[pygame.K_F1] and keys[pygame.K_a]:
            if not((55,55,65,65) in ship_list):
                ship_list.append((55,55,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_a]:
                ship_list.append((120,55,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_a]:
            if not((185,55,65,65) in ship_list):
                ship_list.append((185,55,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_a]:
            if not((250,55,65,65) in ship_list):
                ship_list.append((250,55,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_a]:
            if not((315,55,65,65) in ship_list):
                ship_list.append((315,55,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_a]:
            if not((380,55,65,65) in ship_list):
                ship_list.append((380,55,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_a]:
            if not((445,55,65,65) in ship_list):
                ship_list.append((445,55,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_a]:
            if not((510,55,65,65) in ship_list):
                ship_list.append((510,55,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_a]:
            if not((575,55,65,65) in ship_list):
                ship_list.append((575,55,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_a]:
            if not((640,55,65,65) in ship_list):
                ship_list.append((640,55,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_a]:
            if not((705,55,65,65) in ship_list):
                ship_list.append((705,55,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_a]:
            if not((770,55,65,65) in ship_list):
                ship_list.append((770,55,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_b]:
            if not((55,120,65,65) in ship_list):
                ship_list.append((55,120,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_b]:
            if not((120,120,65,65) in ship_list):
                ship_list.append((120,120,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_b]:
            if not((185,120,65,65) in ship_list):
                ship_list.append((185,120,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_b]:
            if not((250,120,65,65) in ship_list):
                ship_list.append((250,120,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_b]:
            if not((315,120,65,65) in ship_list):
                ship_list.append((315,120,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_b]:
            if not((380,120,65,65) in ship_list):
                ship_list.append((380,120,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_b]:
            if not((445,120,65,65) in ship_list):
                ship_list.append((445,120,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_b]:
            if not((510,120,65,65) in ship_list):
                ship_list.append((510,120,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_b]:
            if not((575,120,65,65) in ship_list):
                ship_list.append((575,120,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_b]:
            if not((640,120,65,65) in ship_list):
                ship_list.append((640,120,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_b]:
            if not((705,120,65,65) in ship_list):
                ship_list.append((705,120,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_b]:
            if not((770,120,65,65) in ship_list):
                ship_list.append((770,120,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_c]:
            if not((55,185,65,65) in ship_list):
                ship_list.append((55,185,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_c]:
            if not((120,185,65,65) in ship_list):
                ship_list.append((120,185,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_c]:
            if not((185,185,65,65) in ship_list):
                ship_list.append((185,185,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_c]:
            if not((250,185,65,65) in ship_list):
                ship_list.append((250,185,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_c]:
            if not((315,185,65,65) in ship_list):
                ship_list.append((315,185,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_c]:
            if not((380,185,65,65) in ship_list):
                ship_list.append((380,185,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_c]:
            if not((445,185,65,65) in ship_list):
                ship_list.append((445,185,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_c]:
            if not((510,185,65,65) in ship_list):
                ship_list.append((510,185,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_c]:
            if not((575,185,65,65) in ship_list):
                ship_list.append((575,185,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_c]:
            if not((640,185,65,65) in ship_list):
                ship_list.append((640,185,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_c]:
            if not((705,185,65,65) in ship_list):
                ship_list.append((705,185,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_c]:
            if not((770,185,65,65) in ship_list):
                ship_list.append((770,185,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_d]:
            if not((55,250,65,65) in ship_list):
                ship_list.append((55,250,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_d]:
            if not((120,250,65,65) in ship_list):
                ship_list.append((120,250,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_d]:
            if not((185,250,65,65) in ship_list):
                ship_list.append((185,250,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_d]:
            if not((250,250,65,65) in ship_list):
                ship_list.append((250,250,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_d]:
            if not((315,250,65,65) in ship_list):
                ship_list.append((315,250,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_d]:
            if not((380,250,65,65) in ship_list):
                ship_list.append((380,250,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_d]:
            if not((445,250,65,65) in ship_list):
                ship_list.append((445,250,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_d]:
            if not((510,250,65,65) in ship_list):
                ship_list.append((510,250,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_d]:
            if not((575,250,65,65) in ship_list):
                ship_list.append((575,250,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_d]:
            if not((640,250,65,65) in ship_list):
                ship_list.append((640,250,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_d]:
            if not((705,250,65,65) in ship_list):
                ship_list.append((705,250,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_d]:
            if not((770,250,65,65) in ship_list):
                ship_list.append((770,250,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_e]:
            if not((55,315,65,65) in ship_list):
                ship_list.append((55,315,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_e]:
            if not((120,315,65,65) in ship_list):
                ship_list.append((120,315,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_e]:
            if not((185,315,65,65) in ship_list):
                ship_list.append((185,315,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_e]:
            if not((250,315,65,65) in ship_list):
                ship_list.append((250,315,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_e]:
            if not((315,315,65,65) in ship_list):
                ship_list.append((315,315,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_e]:
            if not((380,315,65,65) in ship_list):
                ship_list.append((380,315,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_e]:
            if not((445,315,65,65) in ship_list):
                ship_list.append((445,315,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_e]:
            if not((510,315,65,65) in ship_list):
                ship_list.append((510,315,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_e]:
            if not((575,315,65,65) in ship_list):
                ship_list.append((575,315,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_e]:
            if not((640,315,65,65) in ship_list):
                ship_list.append((640,315,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_e]:
            if not((705,315,65,65) in ship_list):
                ship_list.append((705,315,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_e]:
            if not((770,315,65,65) in ship_list):
                ship_list.append((770,315,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_f]:
            if not((55,380,65,65) in ship_list):
                ship_list.append((55,380,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_f]:
            if not((120,380,65,65) in ship_list):
                ship_list.append((120,380,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_f]:
            if not((185,380,65,65) in ship_list):
                ship_list.append((185,380,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_f]:
            if not((250,380,65,65) in ship_list):
                ship_list.append((250,380,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_f]:
            if not((315,380,65,65) in ship_list):
                ship_list.append((315,380,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_f]:
            if not((380,380,65,65) in ship_list):
                ship_list.append((380,380,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_f]:
            if not((445,380,65,65) in ship_list):
                ship_list.append((445,380,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_f]:
            if not((510,380,65,65) in ship_list):
                ship_list.append((510,380,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_f]:
            if not((575,380,65,65) in ship_list):
                ship_list.append((575,380,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_f]:
            if not((640,380,65,65) in ship_list):
                ship_list.append((640,380,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_f]:
            if not((705,380,65,65) in ship_list):
                ship_list.append((705,380,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_f]:
            if not((770,380,65,65) in ship_list):
                ship_list.append((770,380,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_g]:
            if not((55,445,65,65) in ship_list):
                ship_list.append((55,445,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_g]:
            if not((120,445,65,65) in ship_list):
                ship_list.append((120,445,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_g]:
            if not((185,445,65,65) in ship_list):
                ship_list.append((185,445,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_g]:
            if not((250,445,65,65) in ship_list):
                ship_list.append((250,445,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_g]:
            if not((315,445,65,65) in ship_list):
                ship_list.append((315,445,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_g]:
            if not((380,445,65,65) in ship_list):
                ship_list.append((380,445,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_g]:
            if not((445,445,65,65) in ship_list):
                ship_list.append((445,445,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_g]:
            if not((510,445,65,65) in ship_list):
                ship_list.append((510,445,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_g]:
            if not((575,445,65,65) in ship_list):
                ship_list.append((575,445,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_g]:
            if not((640,445,65,65) in ship_list):
                ship_list.append((640,445,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_g]:
            if not((705,445,65,65) in ship_list):
                ship_list.append((705,445,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_g]:
            if not((770,445,65,65) in ship_list):
                ship_list.append((770,445,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_h]:
            if not((55,510,65,65) in ship_list):
                ship_list.append((55,510,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_h]:
            if not((120,510,65,65) in ship_list):
                ship_list.append((120,510,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_h]:
            if not((185,510,65,65) in ship_list):
                ship_list.append((185,510,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_h]:
            if not((250,510,65,65) in ship_list):
                ship_list.append((250,510,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_h]:
            if not((315,510,65,65) in ship_list):
                ship_list.append((315,510,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_h]:
            if not((380,510,65,65) in ship_list):
                ship_list.append((380,510,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_h]:
            if not((445,510,65,65) in ship_list):
                ship_list.append((445,510,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_h]:
            if not((510,510,65,65) in ship_list):
                ship_list.append((510,510,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_h]:
            if not((575,510,65,65) in ship_list):
                ship_list.append((575,510,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_h]:
            if not((640,510,65,65) in ship_list):
                ship_list.append((640,510,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_h]:
            if not((705,510,65,65) in ship_list):
                ship_list.append((705,510,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_h]:
            if not((770,510,65,65) in ship_list):
                ship_list.append((770,510,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_i]:
            if not((55,575,65,65) in ship_list):
                ship_list.append((55,575,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_i]:
            if not((120,575,65,65) in ship_list):
                ship_list.append((120,575,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_i]:
            if not((185,575,65,65) in ship_list):
                ship_list.append((185,575,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_i]:
            if not((250,575,65,65) in ship_list):
                ship_list.append((250,575,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_i]:
            if not((315,575,65,65) in ship_list):
                ship_list.append((315,575,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_i]:
            if not((380,575,65,65) in ship_list):
                ship_list.append((380,575,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_i]:
            if not((445,575,65,65) in ship_list):
                ship_list.append((445,575,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_i]:
            if not((510,575,65,65) in ship_list):
                ship_list.append((510,575,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_i]:
            if not((575,575,65,65) in ship_list):
                ship_list.append((575,575,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_i]:
            if not((640,575,65,65) in ship_list):
                ship_list.append((640,575,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_i]:
            if not((705,575,65,65) in ship_list):
                ship_list.append((705,575,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_i]:
            if not((770,575,65,65) in ship_list):
                ship_list.append((770,575,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_j]:
            if not((55,640,65,65) in ship_list):
                ship_list.append((55,640,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_j]:
            if not((120,640,65,65) in ship_list):
                ship_list.append((120,640,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_j]:
            if not((185,640,65,65) in ship_list):
                ship_list.append((185,640,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_j]:
            if not((250,640,65,65) in ship_list):
                ship_list.append((250,640,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_j]:
            if not((315,640,65,65) in ship_list):
                ship_list.append((315,640,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_j]:
            if not((380,640,65,65) in ship_list):
                ship_list.append((380,640,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_j]:
            if not((445,640,65,65) in ship_list):
                ship_list.append((445,640,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_j]:
            if not((510,640,65,65) in ship_list):
                ship_list.append((510,640,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_j]:
            if not((575,640,65,65) in ship_list):
                ship_list.append((575,640,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_j]:
            if not((640,640,65,65) in ship_list):
                ship_list.append((640,640,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_j]:
            if not((705,640,65,65) in ship_list):
                ship_list.append((705,640,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_j]:
            if not((770,640,65,65) in ship_list):
                ship_list.append((770,640,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_k]:
            if not((55,705,65,65) in ship_list):
                ship_list.append((55,705,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_k]:
            if not((120,705,65,65) in ship_list):
                ship_list.append((120,705,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_k]:
            if not((185,705,65,65) in ship_list):
                ship_list.append((185,705,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_k]:
            if not((250,705,65,65) in ship_list):
                ship_list.append((250,705,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_k]:
            if not((315,705,65,65) in ship_list):
                ship_list.append((315,705,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_k]:
            if not((380,705,65,65) in ship_list):
                ship_list.append((380,705,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_k]:
            if not((445,705,65,65) in ship_list):
                ship_list.append((445,705,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_k]:
            if not((510,705,65,65) in ship_list):
                ship_list.append((510,705,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_k]:
            if not((575,705,65,65) in ship_list):
                ship_list.append((575,705,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_k]:
            if not((640,705,65,65) in ship_list):
                ship_list.append((640,705,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_k]:
            if not((705,705,65,65) in ship_list):
                ship_list.append((705,705,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_k]:
            if not((770,705,65,65) in ship_list):
                ship_list.append((770,705,65,65))
        elif keys[pygame.K_F1] and keys[pygame.K_l]:
            if not((55,770,65,65) in ship_list):
                ship_list.append((55,770,65,65))
        elif keys[pygame.K_F2] and keys[pygame.K_l]:
            if not((120,770,65,65) in ship_list):
                ship_list.append((120,770,65,65))
        elif keys[pygame.K_F3] and keys[pygame.K_l]:
            if not((185,770,65,65) in ship_list):
                ship_list.append((185,770,65,65))
        elif keys[pygame.K_F4] and keys[pygame.K_l]:
            if not((250,770,65,65) in ship_list):
                ship_list.append((250,770,65,65))
        elif keys[pygame.K_F5] and keys[pygame.K_l]:
            if not((315,770,65,65) in ship_list):
                ship_list.append((315,770,65,65))
        elif keys[pygame.K_F6] and keys[pygame.K_l]:
            if not((380,770,65,65) in ship_list):
                ship_list.append((380,770,65,65))
        elif keys[pygame.K_F7] and keys[pygame.K_l]:
            if not((445,770,65,65) in ship_list):
                ship_list.append((445,770,65,65))
        elif keys[pygame.K_F8] and keys[pygame.K_l]:
            if not((510,770,65,65) in ship_list):
                ship_list.append((510,770,65,65))
        elif keys[pygame.K_F9] and keys[pygame.K_l]:
            if not((575,770,65,65) in ship_list):
                ship_list.append((575,770,65,65))
        elif keys[pygame.K_F10] and keys[pygame.K_l]:
            if not((640,770,65,65) in ship_list):
                ship_list.append((640,770,65,65))
        elif keys[pygame.K_F11] and keys[pygame.K_l]:
            if not((705,770,65,65) in ship_list):
                ship_list.append((705,770,65,65))
        elif keys[pygame.K_F12] and keys[pygame.K_l]:
            if not((770,770,65,65) in ship_list):
                ship_list.append((770,770,65,65))
    return ship_list