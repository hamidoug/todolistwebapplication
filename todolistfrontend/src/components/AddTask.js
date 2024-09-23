import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addTask } from '../features/tasks/tasksSlice';
import { useForm } from 'react-hook-form'


const AddTask = () => {
    const dispatch = useDispatch();
    const { register, handleSubmit, reset, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        dispatch(addTask(data)); 
        reset(); 
    };

    return (
        <div className="search">
            <form onSubmit={handleSubmit(onSubmit)}>
                <label>
                    Task:
                    <input type="text" name="title" placeholder='Enter Task Name' {...register("title", { required: true })} />
                </label>
                <label>
                    Description:
                    <input type="text" name="description" placeholder='Enter Description' {...register("description", { required: true })} />
                </label>
                <label>
                    Due Date:
                    <input type="date" name="due_date" {...register("due_date", { required: true })} />
                </label>
                <button type="submit">Add Task</button>
            </form>
            {errors.title?.type === "required" && <small>This field cannot be blank</small>}
            {errors.description?.type === "required" && <small>This field cannot be blank</small>}
            {errors.due_date?.type === "required" && <small>This field cannot be blank</small>}
        </div>
    );
};

export default AddTask;