from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
sendbuf=[]
root=0
size = comm.size
rank = comm.rank

if rank==0:
	matrix=numpy.array(range(size*size),dtype=float)
	matrix.shape=(size,size)
	print(matrix,rank)
	sendbuf=matrix

v=comm.scatter(sendbuf,root)
print("I got this array:")
print(v)
v=v*v

recvbuf=comm.gather(v,root)
if rank==0:
	print(numpy.array(recvbuf))
if rank==0:
	sendbuf="done"

recvbuf=MPI.COMM_WORLD.bcast(sendbuf,root)
print(recvbuf)