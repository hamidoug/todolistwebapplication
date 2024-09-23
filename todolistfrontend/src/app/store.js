import { configureStore } from '@reduxjs/toolkit';
import tasksReducer from '../features/tasks/tasksSlice';

//Configure store used to set up store
export default configureStore({
    reducer: {
        tasks: tasksReducer,
    }, 
})