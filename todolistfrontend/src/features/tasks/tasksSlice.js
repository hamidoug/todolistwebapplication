import { createSlice, createAsyncThunk, createSelector } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchTasks = createAsyncThunk('tasks/fetchTasks', async () =>
{
    const response = await axios.get('/api/tasks/')
    return response.data
});

export const addTask = createAsyncThunk('tasks/addTask', async (task) =>
{
    const response = await axios.post('/api/tasks/', task)
    return response.data
});

export const deleteTask = createAsyncThunk('tasks/deleteTask', async (taskId) =>
{
    await axios.delete('/api/tasks/${taskId}')
    return taskId
});

export const updateTask = createAsyncThunk('tasks/updateTask', async (task) =>
{
    const response = await axios.put('/api/tasks/${task.id}', task)
    return response.data
});

export const tasksSlice = createSlice({
    name: 'tasks',
    initialState: {
        tasks: [],
        status: 'idle',
        error: null,
    },

    reducers: {},
    extraReducers: (builder) => {
        builder
        .addCase(fetchTasks.fulfilled, (state, action) => {
            state.tasks = action.payload;
        })
        .addCase(addTask.fulfilled, (state, action) => {
            state.tasks.push(action.payload);
        })
        .addCase(deleteTask.fulfilled, (state, action) => {
            state.tasks = state.tasks.filter(task => task.id !== action.payload);
        })
        .addCase(updateTask.fulfilled, (state, action) => {
            const index = state.tasks.findIndex(task => task.id === action.payload.id);
            if (index !== -1) {
                state.tasks[index] = action.payload;
            }
        });
    },
});

export default tasksSlice.reducer;