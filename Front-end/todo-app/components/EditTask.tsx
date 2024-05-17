export default function EditTask() {
    return (
      <form className=" flex flex-col gap-x-3 w-full">
        <input
          type="text"
          placeholder=" Add Task here"
          minLength={3}
          maxLength={54}
          required
          name="Edit_Task"
          className=" w-full px-2 py-1 border border-gray-100 rounded-md"
        />
        <button className=" px-2 py-1 bg-teal-600 text-white rounded-md w-full mt-4">Save</button>
      </form>
    );
  }
  