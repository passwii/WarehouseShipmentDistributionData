"""
美国各州缩写和全称映射字典
"""

# 美国50个州的全称到缩写映射
us_state_abbrev = {
    # 美国50个州
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    
    # 美国属地和联邦地区
    'District of Columbia': 'DC',  # 华盛顿哥伦比亚特区
    'American Samoa': 'AS',        # 美属萨摩亚
    'Guam': 'GU',                  # 关岛
    'Northern Mariana Islands': 'MP',  # 北马里亚纳群岛
    'Puerto Rico': 'PR',           # 波多黎各
    'U.S. Virgin Islands': 'VI'    # 美属维尔京群岛
}

# 缩写到全称的映射（用于将缩写转换为全称）
abbrev_to_state = {v: k for k, v in us_state_abbrev.items()}

# 全称大写到标准格式的映射（用于将大写全称转换为标准格式）
state_to_standard = {
    'ALABAMA': 'Alabama', 'ALASKA': 'Alaska', 'ARIZONA': 'Arizona', 'ARKANSAS': 'Arkansas',
    'CALIFORNIA': 'California', 'COLORADO': 'Colorado', 'CONNECTICUT': 'Connecticut', 'DELAWARE': 'Delaware',
    'FLORIDA': 'Florida', 'GEORGIA': 'Georgia', 'HAWAII': 'Hawaii', 'IDAHO': 'Idaho',
    'ILLINOIS': 'Illinois', 'INDIANA': 'Indiana', 'IOWA': 'Iowa', 'KANSAS': 'Kansas',
    'KENTUCKY': 'Kentucky', 'LOUISIANA': 'Louisiana', 'MAINE': 'Maine', 'MARYLAND': 'Maryland',
    'MASSACHUSETTS': 'Massachusetts', 'MICHIGAN': 'Michigan', 'MINNESOTA': 'Minnesota', 'MISSISSIPPI': 'Mississippi',
    'MISSOURI': 'Missouri', 'MONTANA': 'Montana', 'NEBRASKA': 'Nebraska', 'NEVADA': 'Nevada',
    'NEW HAMPSHIRE': 'New Hampshire', 'NEW JERSEY': 'New Jersey', 'NEW MEXICO': 'New Mexico', 'NEW YORK': 'New York',
    'NORTH CAROLINA': 'North Carolina', 'NORTH DAKOTA': 'North Dakota', 'OHIO': 'Ohio', 'OKLAHOMA': 'Oklahoma',
    'OREGON': 'Oregon', 'PENNSYLVANIA': 'Pennsylvania', 'RHODE ISLAND': 'Rhode Island', 'SOUTH CAROLINA': 'South Carolina',
    'SOUTH DAKOTA': 'South Dakota', 'TENNESSEE': 'Tennessee', 'TEXAS': 'Texas', 'UTAH': 'Utah',
    'VERMONT': 'Vermont', 'VIRGINIA': 'Virginia', 'WASHINGTON': 'Washington', 'WEST VIRGINIA': 'West Virginia',
    'WISCONSIN': 'Wisconsin', 'WYOMING': 'Wyoming',
    # 属地
    'DISTRICT OF COLUMBIA': 'District of Columbia', 'AMERICAN SAMOA': 'American Samoa', 'GUAM': 'Guam',
    'NORTHERN MARIANA ISLANDS': 'Northern Mariana Islands', 'PUERTO RICO': 'Puerto Rico', 'U.S. VIRGIN ISLANDS': 'U.S. Virgin Islands'
}

# 英文州名到中文翻译的映射
state_to_chinese = {
    'Alabama': '阿拉巴马州',
    'Alaska': '阿拉斯加州',
    'Arizona': '亚利桑那州',
    'Arkansas': '阿肯色州',
    'California': '加利福尼亚州',
    'Colorado': '科罗拉多州',
    'Connecticut': '康涅狄格州',
    'Delaware': '特拉华州',
    'Florida': '佛罗里达州',
    'Georgia': '佐治亚州',
    'Hawaii': '夏威夷州',
    'Idaho': '爱达荷州',
    'Illinois': '伊利诺伊州',
    'Indiana': '印第安纳州',
    'Iowa': '艾奥瓦州',
    'Kansas': '堪萨斯州',
    'Kentucky': '肯塔基州',
    'Louisiana': '路易斯安那州',
    'Maine': '缅因州',
    'Maryland': '马里兰州',
    'Massachusetts': '马萨诸塞州',
    'Michigan': '密歇根州',
    'Minnesota': '明尼苏达州',
    'Mississippi': '密西西比州',
    'Missouri': '密苏里州',
    'Montana': '蒙大拿州',
    'Nebraska': '内布拉斯加州',
    'Nevada': '内华达州',
    'New Hampshire': '新罕布什尔州',
    'New Jersey': '新泽西州',
    'New Mexico': '新墨西哥州',
    'New York': '纽约州',
    'North Carolina': '北卡罗来纳州',
    'North Dakota': '北达科他州',
    'Ohio': '俄亥俄州',
    'Oklahoma': '俄克拉何马州',
    'Oregon': '俄勒冈州',
    'Pennsylvania': '宾夕法尼亚州',
    'Rhode Island': '罗得岛州',
    'South Carolina': '南卡罗来纳州',
    'South Dakota': '南达科他州',
    'Tennessee': '田纳西州',
    'Texas': '得克萨斯州',
    'Utah': '犹他州',
    'Vermont': '佛蒙特州',
    'Virginia': '弗吉尼亚州',
    'Washington': '华盛顿州',
    'West Virginia': '西弗吉尼亚州',
    'Wisconsin': '威斯康星州',
    'Wyoming': '怀俄明州',
    # 属地
    'District of Columbia': '华盛顿哥伦比亚特区',
    'American Samoa': '美属萨摩亚',
    'Guam': '关岛',
    'Northern Mariana Islands': '北马里亚纳群岛',
    'Puerto Rico': '波多黎各',
    'U.S. Virgin Islands': '美属维尔京群岛'
}

# 州到区域的映射字典
state_to_region = {
    # 美西 (以CA为核心)
    'California': '美西',
    'Oregon': '美西',
    'Washington': '美西',
    'Nevada': '美西',
    'Arizona': '美西',
    'Idaho': '美西',
    'Montana': '美西',
    'Wyoming': '美西',
    'Utah': '美西',
    'Colorado': '美西',
    'Alaska': '美西',
    'Hawaii': '美西',
    
    # 美中 (以TX为核心)
    'Texas': '美中',
    'Oklahoma': '美中',
    'Kansas': '美中',
    'Nebraska': '美中',
    'South Dakota': '美中',
    'North Dakota': '美中',
    'Minnesota': '美中',
    'Iowa': '美中',
    'Missouri': '美中',
    'Arkansas': '美中',
    'Louisiana': '美中',
    'Illinois': '美中',
    'Indiana': '美中',
    'Michigan': '美中',
    'Wisconsin': '美中',
    'Ohio': '美中',
    
    # 美南 (以FL为核心)
    'Florida': '美南',
    'Georgia': '美南',
    'South Carolina': '美南',
    'North Carolina': '美南',
    'Virginia': '美南',
    'West Virginia': '美南',
    'Kentucky': '美南',
    'Tennessee': '美南',
    'Mississippi': '美南',
    'Alabama': '美南',
    
    # 美东 (以NJ和NY为核心)
    'New York': '美东',
    'New Jersey': '美东',
    'Pennsylvania': '美东',
    'Delaware': '美东',
    'Maryland': '美东',
    'District of Columbia': '美东',
    'Connecticut': '美东',
    'Rhode Island': '美东',
    'Massachusetts': '美东',
    'Vermont': '美东',
    'New Hampshire': '美东',
    'Maine': '美东'
}