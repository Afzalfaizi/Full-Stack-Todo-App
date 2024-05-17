import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import AddTask from "./AddTask"

export function Modal() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="default" className=" w-full bg-teal-600 px-2 py-1 text-white uppercase text-lg ">Add Task</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Add New Task</DialogTitle>
        </DialogHeader>
        <AddTask/>
    
      </DialogContent>
    </Dialog>
  )
}
