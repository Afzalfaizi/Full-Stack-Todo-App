'use client'
import { add_todo } from "@/app/actions";
import { useFormState } from "react-dom";
import { useEffect } from "react";
import { useRef } from "react";
import toast from "react-hot-toast";



export default function AddTask() {
  const ref = useRef<HTMLFormElement>(null)
  const [state, formAction] = useFormState(add_todo,{status:" ", message:" "})
  const {status, message} = state;

  
  useEffect(()=>{
    if(status == 'success'){
      ref.current?.reset()
      toast.success(message)
    } else if (status == 'error'){ 
      toast.error(message)
    }
  },[state])


  return (
    <form ref={ref} action={formAction} className=" flex flex-col gap-x-3 w-full">
      <input
        type="text"
        placeholder=" Add Task here"
        minLength={3}
        maxLength={54}
        required
        name="Add_Task"
        className=" w-full px-2 py-1 border border-gray-100 rounded-md"
      />
      <button className=" px-2 py-1 bg-teal-600 text-white rounded-md w-full mt-4">Save</button>
    </form>
  );
}
