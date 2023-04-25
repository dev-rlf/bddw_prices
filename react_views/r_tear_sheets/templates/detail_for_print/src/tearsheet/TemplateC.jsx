import {useEffect, useRef, useState} from 'react'

//RULE DISPLAY ABOVE
//RULE DISPLAY ABOVE
//RULE DISPLAY ABOVE
//RULE DISPLAY ABOVE
export default function TemplateC({price_records, sdata}) {
	return(
		<>
		<div style={{'height': sdata.pt_pr}}></div>
				{/*iterate over the price records objects, each objectL key == rule type, value = the list of price record objects*/}
				{  price_records.map(  ( obj )  => { return( Object.entries(obj).map( ([key, value]) => { return( <RuleTypeGroup sdata={sdata} price_records={value} rule_type={key} />)})) })}
	</>
	)
}

function RuleTypeGroup({sdata, price_records, rule_type}) {
  return(
		<table style={{'width': '666px'}} className={`mx-auto table-auto`}>
			<thead className="text-gray-400 text-left">
				<th style={{'font-weight': 'normal', 'width': `${sdata.col_1}%`}} className="py-1">{rule_type}</th>
				<th></th>
				<th style={{'font-weight': 'normal'}} className="py-1">LIST</th>
				<th style={{'font-weight': 'normal'}} className="py-1">NET</th>
			</thead>
			<tbody>
				{ price_records.map( (price_record, index) =>  <TableRow sdata={sdata} index={index} price_record={price_record} />)}
			</tbody>
		</table>
	)
}

function TableRow({sdata, price_record, index}) {

	const [rule_type, setRecord] = useState(price_record.rule_type)
	const [display_one, setOne] = useState(price_record.rule_display_1)
	const [display_two, setTwo] = useState(price_record.rule_display_2)
	const [list, setList] = useState(price_record.list_price)
	const [net, setNet] = useState(price_record.net_price)

  return(
		<>
			<tr key={index} className="hover:bg-gray-50 text-gray-400 text-left">
					<td style={{'width':`${sdata.col_2}%`}} >{display_one}</td>
					<td style={{'width':`${sdata.col_3}%`}}>{display_two}</td>
					<td style={{'width':`${sdata.col_4}%`}}>${list}</td>
					<td style={{'width':`${sdata.col_5}%`}}>${net}</td>
			</tr>
		</>
	)
}