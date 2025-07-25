import keyboard


class InputHandler:

    def get_actions(self) -> set:
        """Poll real-time key states using the keyboard module."""
        actions = set()
        if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
            actions.add('left')
        if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
            actions.add('right')
        if keyboard.is_pressed('w') or keyboard.is_pressed('space') or keyboard.is_pressed('up'):
            actions.add('jump')
        if keyboard.is_pressed('q'):
            actions.add('quit')
        return actions
