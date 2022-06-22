from sympy import *
import pfnn_toolkit as hp
import numpy as np
import torch
import sys
import pfnn_toolkit.distributed as dist
import possion


def get_handle():
    rhs_handle = hp.expression.BCHandle()
    bd_handle = hp.expression.BCHandle()

    t, x1, x2, x3 = symbols('t x1 x2 x3')

    # Equations here.
    u = (x1**2 - 1) * (x2**2 - 1) * (x3**2 - 1) * exp(-1 * t)
    r = diff(u, t) - (diff(u, x1, 2) + diff(u, x2, 2) + diff(u, x3, 2))

    rhs_handle.var = (t, x1, x2, x3)
    bd_handle.var = (t, x1, x2, x3)
    rhs_handle.expr = [r]
    bd_handle.expr = [u]
    return rhs_handle, bd_handle


def main():
    args = hp.init()

    # Initialize the geometry
    rhs_handle, boundary_handle = get_handle()
    geo = hp.geometry.TrimeshGeometry.from_csv(
        faces_ind_file="3d_irregular/faces_ind.csv",
        vertices_file="3d_irregular/vertices.csv",
        t_sup=1.0,
        t_inf=0.0,
        dtype=np.float64)

    decomposed_geo = hp.geometry.DecomposedGeometry(
        geometry=geo, subdomain_num=args.subdomain_num)

    # Initialize the datasets
    train_dataset = hp.data.GeometryTrainDataset(geometry=decomposed_geo)

    train_dataset.add_constraint(
        hp.data.Constraint(type='internal',
                           lhs_handle=possion.lhs,
                           rhs_handle=rhs_handle))
    train_dataset.add_constraint(
        hp.data.Constraint(type='dirichlet', rhs_handle=boundary_handle))

    # Setting up the solver.
    solver = hp.train.PFNNSolver(train_dataset=train_dataset,
                                 geometry=decomposed_geo)

    solver.solve()


if __name__ == "__main__":
    main()
