from classes.state import state_class


async def light_loop(internal_state: state_class):
    while internal_state.running:
        # Wait for a new message
        await internal_state.new_message_event.wait()
        internal_state.new_message_event.clear()


        if internal_state.current_effect is None:
            # do basic light thing
            internal_state.light.set_colour(
                internal_state.light_state["colour"]
                )
            internal_state.light.set_brightness(
                internal_state.light_state["brightness"]
            )

        else:
            internal_state.light.set_colour(
                internal_state.light_state["colour"]    
                )
            # run the effect to update the light bitmap
            internal_state.current_effect.code(internal_state.bitmap)
            internal_state.light.render_bitmap(internal_state.bitmap)
        
        # Signal that we have processed the new state
        internal_state.state_processed_event.set()
