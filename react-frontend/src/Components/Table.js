import React from 'react'


import {
createColumnHelper,
flexRender,
getCoreRowModel,
useReactTable,
} from '@tanstack/react-table'




const columnHelper = createColumnHelper()



const Table = ({data, numDims}) => {
    console.log(numDims)
    let dims = []
    for (let i = 0; i < numDims; i++) { // [ {}, {}, {}, {}, {}, {}, {}, {}, {}, {} ]
        dims.push(i)

    }
    const columns = dims.map((dim) => columnHelper.accessor(dim.toString(), {
        cell: info => <i>{info.getValue()}</i>, 
        header: () => <span>{dim}</span>
    })).concat(columnHelper.accessor(numDims.toString(), {
        cell: info => <i>{info.getValue()}</i>,
        header: () => <span>#</span>
    }))

    console.log(dims)
    console.log(columns)
    console.log(typeof(data))

    const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
    })

    return (
        <div id="p-2">
        <table>
            <thead>
            {table.getHeaderGroups().map(headerGroup => (
                <tr key={headerGroup.id}>
                {headerGroup.headers.map(header => (
                    <th key={header.id}>
                    {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                        )}
                    </th>
                ))}
                </tr>
            ))}
            </thead>
            <tbody>
            {table.getRowModel().rows.map(row => (
                <tr key={row.id}>
                {row.getVisibleCells().map(cell => (
                    <td key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                    </td>
                ))}
                </tr>
            ))}
            </tbody>

        </table>
        </div>
    )
}

export default Table