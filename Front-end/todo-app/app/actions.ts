"use server";

import { revalidatePath } from "next/cache";

// Add Todo Function
export async function add_todo(
  state: {status: string; message: string },
  formData: FormData
) {
  const new_todo = formData.get("add_task") as string;

  try {
    const response = await fetch("http://127.0.0.1:8080/create_todo/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({task: new_todo,})
    });
    revalidatePath('/create_todo/')
    return { status: "success", message: "Todo added successfully" };
  } catch (error) {
    return { status: "error", message: "Something went wrong" };
  }
}
