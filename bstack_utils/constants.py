# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import re
from enum import Enum
bstack1ll1l1l11l_opy_ = {
  bstack11l11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧ្ࠪ"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷ࠭៓"),
  bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭។"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡯ࡪࡿࠧ៕"),
  bstack11l11ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ៖"): bstack11l11ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪៗ"),
  bstack11l11ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ៘"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨ៙"),
  bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ៚"): bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࠫ៛"),
  bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧៜ"): bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫ៝"),
  bstack11l11ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ៞"): bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ៟"),
  bstack11l11ll_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧ០"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭ࠧ១"),
  bstack11l11ll_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨ២"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡳࡰ࡮ࡨࠫ៣"),
  bstack11l11ll_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪ៤"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪ៥"),
  bstack11l11ll_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫ៦"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫ៧"),
  bstack11l11ll_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨ៨"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡹ࡭ࡩ࡫࡯ࠨ៩"),
  bstack11l11ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪ៪"): bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪ៫"),
  bstack11l11ll_opy_ (u"࠭ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭៬"): bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭៭"),
  bstack11l11ll_opy_ (u"ࠨࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭៮"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭៯"),
  bstack11l11ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡻࡱࡱࡩࠬ៰"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸ࡮ࡳࡥࡻࡱࡱࡩࠬ៱"),
  bstack11l11ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ៲"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ៳"),
  bstack11l11ll_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭៴"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭៵"),
  bstack11l11ll_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ៶"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ៷"),
  bstack11l11ll_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫ៸"): bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫ៹"),
  bstack11l11ll_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨ៺"): bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦࡰࡧࡏࡪࡿࡳࠨ៻"),
  bstack11l11ll_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡡࡪࡶࠪ៼"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴ࡝ࡡࡪࡶࠪ៽"),
  bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡹࡴࡴࠩ៾"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡬ࡴࡹࡴࡴࠩ៿"),
  bstack11l11ll_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ࠭᠀"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡦࡤࡣࡦ࡬ࡪ࠭᠁"),
  bstack11l11ll_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨ᠂"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨ᠃"),
  bstack11l11ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬ᠄"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬ᠅"),
  bstack11l11ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ᠆"): bstack11l11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ᠇"),
  bstack11l11ll_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪ᠈"): bstack11l11ll_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬ᠉"),
  bstack11l11ll_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᠊"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᠋"),
  bstack11l11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪ᠌"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪ᠍"),
  bstack11l11ll_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭᠎"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭᠏"),
  bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭᠐"): bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩ᠑"),
  bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᠒"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᠓"),
  bstack11l11ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ᠔"): bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸࡵࡵࡳࡥࡨࠫ᠕"),
  bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᠖"): bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᠗"),
  bstack11l11ll_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪ᠘"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡔࡡ࡮ࡧࠪ᠙"),
  bstack11l11ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭᠚"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭᠛"),
  bstack11l11ll_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᠜"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᠝"),
  bstack11l11ll_opy_ (u"ࠧࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬ᠞"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬ᠟"),
  bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᠠ"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᠡ"),
  bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᠢ"): bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᠣ")
}
bstack11l1l111111_opy_ = [
  bstack11l11ll_opy_ (u"࠭࡯ࡴࠩᠤ"),
  bstack11l11ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᠥ"),
  bstack11l11ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᠦ"),
  bstack11l11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᠧ"),
  bstack11l11ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᠨ"),
  bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᠩ"),
  bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᠪ"),
]
bstack11lllll11l_opy_ = {
  bstack11l11ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᠫ"): [bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᠬ"), bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡔࡁࡎࡇࠪᠭ")],
  bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᠮ"): bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ᠯ"),
  bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᠰ"): bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠨᠱ"),
  bstack11l11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᠲ"): bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠬᠳ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᠴ"): bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᠵ"),
  bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᠶ"): bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡘࡥࡐࡆࡔࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᠷ"),
  bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᠸ"): bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࠫᠹ"),
  bstack11l11ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᠺ"): bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬᠻ"),
  bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࠭ᠼ"): [bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕࡥࡉࡅࠩᠽ"), bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖࠧᠾ")],
  bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᠿ"): bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡙ࡄࡌࡡࡏࡓࡌࡒࡅࡗࡇࡏࠫᡀ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡁ"): bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᡂ"),
  bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᡃ"): [bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡐࡄࡖࡉࡗ࡜ࡁࡃࡋࡏࡍ࡙࡟ࠧᡄ"), bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫᡅ")],
  bstack11l11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᡆ"): bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡕࡓࡄࡒࡗࡈࡇࡌࡆࠩᡇ"),
  bstack11l11ll_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡇࡑ࡚ࠬᡈ"): bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡍࡔࡔ࡟ࡔࡏࡄࡖ࡙ࡥࡓࡆࡎࡈࡇ࡙ࡏࡏࡏࡡࡉࡉࡆ࡚ࡕࡓࡇࡢࡆࡗࡇࡎࡄࡊࡈࡗࠬᡉ")
}
bstack111l1ll111_opy_ = {
  bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᡊ"): [bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸ࡟࡯ࡣࡰࡩࠬᡋ"), bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᡌ")],
  bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᡍ"): [bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷࡤࡱࡥࡺࠩᡎ"), bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᡏ")],
  bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᡐ"): bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᡑ"),
  bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᡒ"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᡓ"),
  bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᡔ"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᡕ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᡖ"): [bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡲࡳࠫᡗ"), bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᡘ")],
  bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᡙ"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩᡚ"),
  bstack11l11ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᡛ"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᡜ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࠫᡝ"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳࠫᡞ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫᡟ"): bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫᡠ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᡡ"): bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᡢ"),
  bstack11l11ll_opy_ (u"ࠨࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࡄࡎࡌࠦᡣ"): bstack11l11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࠧᡤ"),
}
bstack1lll1llll1_opy_ = {
  bstack11l11ll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫᡥ"): bstack11l11ll_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᡦ"),
  bstack11l11ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᡧ"): [bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᡨ"), bstack11l11ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᡩ")],
  bstack11l11ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᡪ"): bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᡫ"),
  bstack11l11ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᡬ"): bstack11l11ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᡭ"),
  bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᡮ"): [bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᡯ"), bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫᡰ")],
  bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᡱ"): bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡲ"),
  bstack11l11ll_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬᡳ"): bstack11l11ll_opy_ (u"ࠩࡵࡩࡦࡲ࡟࡮ࡱࡥ࡭ࡱ࡫ࠧᡴ"),
  bstack11l11ll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᡵ"): [bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᡶ"), bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᡷ")],
  bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹࡏ࡮ࡴࡧࡦࡹࡷ࡫ࡃࡦࡴࡷࡷࠬᡸ"): [bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࡳࠨ᡹"), bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࠨ᡺")]
}
bstack111111111_opy_ = [
  bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨ᡻"),
  bstack11l11ll_opy_ (u"ࠪࡴࡦ࡭ࡥࡍࡱࡤࡨࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭᡼"),
  bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ᡽"),
  bstack11l11ll_opy_ (u"ࠬࡹࡥࡵ࡙࡬ࡲࡩࡵࡷࡓࡧࡦࡸࠬ᡾"),
  bstack11l11ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡳࡺࡺࡳࠨ᡿"),
  bstack11l11ll_opy_ (u"ࠧࡴࡶࡵ࡭ࡨࡺࡆࡪ࡮ࡨࡍࡳࡺࡥࡳࡣࡦࡸࡦࡨࡩ࡭࡫ࡷࡽࠬᢀ"),
  bstack11l11ll_opy_ (u"ࠨࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡔࡷࡵ࡭ࡱࡶࡅࡩ࡭ࡧࡶࡪࡱࡵࠫᢁ"),
  bstack11l11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᢂ"),
  bstack11l11ll_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨᢃ"),
  bstack11l11ll_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬᢄ"),
  bstack11l11ll_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᢅ"),
  bstack11l11ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧᢆ"),
]
bstack1l111ll1l_opy_ = [
  bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᢇ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᢈ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨᢉ"),
  bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᢊ"),
  bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᢋ"),
  bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᢌ"),
  bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᢍ"),
  bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᢎ"),
  bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᢏ"),
  bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧᢐ"),
  bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᢑ"),
  bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠫᢒ"),
  bstack11l11ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠧᢓ"),
  bstack11l11ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡚ࡡࡨࠩᢔ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᢕ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᢖ"),
  bstack11l11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᢗ"),
  bstack11l11ll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠲ࠩᢘ"),
  bstack11l11ll_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠴ࠪᢙ"),
  bstack11l11ll_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠶ࠫᢚ"),
  bstack11l11ll_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠸ࠬᢛ"),
  bstack11l11ll_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠺࠭ᢜ"),
  bstack11l11ll_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠼ࠧᢝ"),
  bstack11l11ll_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠷ࠨᢞ"),
  bstack11l11ll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠹ࠩᢟ"),
  bstack11l11ll_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠻ࠪᢠ"),
  bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᢡ"),
  bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬᢢ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᢣ"),
  bstack11l11ll_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪᢤ"),
  bstack11l11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ᢥ"),
  bstack11l11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᢦ"),
  bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᢧ"),
  bstack11l11ll_opy_ (u"ࠬ࡮ࡵࡣࡔࡨ࡫࡮ࡵ࡮ࠨᢨ")
]
bstack11l1l11l111_opy_ = [
  bstack11l11ll_opy_ (u"࠭ࡵࡱ࡮ࡲࡥࡩࡓࡥࡥ࡫ࡤᢩࠫ"),
  bstack11l11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᢪ"),
  bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᢫"),
  bstack11l11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᢬"),
  bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡑࡴ࡬ࡳࡷ࡯ࡴࡺࠩ᢭"),
  bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᢮"),
  bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡦ࡭ࠧ᢯"),
  bstack11l11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᢰ"),
  bstack11l11ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᢱ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᢲ"),
  bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᢳ"),
  bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᢴ"),
  bstack11l11ll_opy_ (u"ࠫࡴࡹࠧᢵ"),
  bstack11l11ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᢶ"),
  bstack11l11ll_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬᢷ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳ࡜ࡧࡩࡵࠩᢸ"),
  bstack11l11ll_opy_ (u"ࠨࡴࡨ࡫࡮ࡵ࡮ࠨᢹ"),
  bstack11l11ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡺࡰࡰࡨࠫᢺ"),
  bstack11l11ll_opy_ (u"ࠪࡱࡦࡩࡨࡪࡰࡨࠫᢻ"),
  bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡰ࡮ࡸࡸ࡮ࡵ࡮ࠨᢼ"),
  bstack11l11ll_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪᢽ"),
  bstack11l11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡕࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᢾ"),
  bstack11l11ll_opy_ (u"ࠧࡷ࡫ࡧࡩࡴ࠭ᢿ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡲࡔࡦ࡭ࡥࡍࡱࡤࡨ࡙࡯࡭ࡦࡱࡸࡸࠬᣀ"),
  bstack11l11ll_opy_ (u"ࠩࡥࡪࡨࡧࡣࡩࡧࠪᣁ"),
  bstack11l11ll_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᣂ"),
  bstack11l11ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᣃ"),
  bstack11l11ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡫࡮ࡥࡍࡨࡽࡸ࠭ᣄ"),
  bstack11l11ll_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪᣅ"),
  bstack11l11ll_opy_ (u"ࠧ࡯ࡱࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠫᣆ"),
  bstack11l11ll_opy_ (u"ࠨࡥ࡫ࡩࡨࡱࡕࡓࡎࠪᣇ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᣈ"),
  bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡆࡳࡴࡱࡩࡦࡵࠪᣉ"),
  bstack11l11ll_opy_ (u"ࠫࡨࡧࡰࡵࡷࡵࡩࡈࡸࡡࡴࡪࠪᣊ"),
  bstack11l11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᣋ"),
  bstack11l11ll_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᣌ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࡚ࡪࡸࡳࡪࡱࡱࠫᣍ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡲࡆࡱࡧ࡮࡬ࡒࡲࡰࡱ࡯࡮ࡨࠩᣎ"),
  bstack11l11ll_opy_ (u"ࠩࡰࡥࡸࡱࡓࡦࡰࡧࡏࡪࡿࡳࠨᣏ"),
  bstack11l11ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡏࡳ࡬ࡹࠧᣐ"),
  bstack11l11ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡍࡩ࠭ᣑ"),
  bstack11l11ll_opy_ (u"ࠬࡪࡥࡥ࡫ࡦࡥࡹ࡫ࡤࡅࡧࡹ࡭ࡨ࡫ࠧᣒ"),
  bstack11l11ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡖࡡࡳࡣࡰࡷࠬᣓ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡪࡲࡲࡪࡔࡵ࡮ࡤࡨࡶࠬᣔ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ᣕ"),
  bstack11l11ll_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡏࡱࡶ࡬ࡳࡳࡹࠧᣖ"),
  bstack11l11ll_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨᣗ"),
  bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᣘ"),
  bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱࡑࡵࡧࡴࠩᣙ"),
  bstack11l11ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡈࡩࡰ࡯ࡨࡸࡷ࡯ࡣࠨᣚ"),
  bstack11l11ll_opy_ (u"ࠧࡷ࡫ࡧࡩࡴ࡜࠲ࠨᣛ"),
  bstack11l11ll_opy_ (u"ࠨ࡯࡬ࡨࡘ࡫ࡳࡴ࡫ࡲࡲࡎࡴࡳࡵࡣ࡯ࡰࡆࡶࡰࡴࠩᣜ"),
  bstack11l11ll_opy_ (u"ࠩࡨࡷࡵࡸࡥࡴࡵࡲࡗࡪࡸࡶࡦࡴࠪᣝ"),
  bstack11l11ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡑࡵࡧࡴࠩᣞ"),
  bstack11l11ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡉࡤࡱࠩᣟ"),
  bstack11l11ll_opy_ (u"ࠬࡺࡥ࡭ࡧࡰࡩࡹࡸࡹࡍࡱࡪࡷࠬᣠ"),
  bstack11l11ll_opy_ (u"࠭ࡳࡺࡰࡦࡘ࡮ࡳࡥࡘ࡫ࡷ࡬ࡓ࡚ࡐࠨᣡ"),
  bstack11l11ll_opy_ (u"ࠧࡨࡧࡲࡐࡴࡩࡡࡵ࡫ࡲࡲࠬᣢ"),
  bstack11l11ll_opy_ (u"ࠨࡩࡳࡷࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᣣ"),
  bstack11l11ll_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡓࡶࡴ࡬ࡩ࡭ࡧࠪᣤ"),
  bstack11l11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᣥ"),
  bstack11l11ll_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࡆ࡬ࡦࡴࡧࡦࡌࡤࡶࠬᣦ"),
  bstack11l11ll_opy_ (u"ࠬࡾ࡭ࡴࡌࡤࡶࠬᣧ"),
  bstack11l11ll_opy_ (u"࠭ࡸ࡮ࡺࡍࡥࡷ࠭ᣨ"),
  bstack11l11ll_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᣩ"),
  bstack11l11ll_opy_ (u"ࠨ࡯ࡤࡷࡰࡈࡡࡴ࡫ࡦࡅࡺࡺࡨࠨᣪ"),
  bstack11l11ll_opy_ (u"ࠩࡺࡷࡑࡵࡣࡢ࡮ࡖࡹࡵࡶ࡯ࡳࡶࠪᣫ"),
  bstack11l11ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡇࡴࡸࡳࡓࡧࡶࡸࡷ࡯ࡣࡵ࡫ࡲࡲࡸ࠭ᣬ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡶࡰࡗࡧࡵࡷ࡮ࡵ࡮ࠨᣭ"),
  bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᣮ"),
  bstack11l11ll_opy_ (u"࠭ࡲࡦࡵ࡬࡫ࡳࡇࡰࡱࠩᣯ"),
  bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡰ࡬ࡱࡦࡺࡩࡰࡰࡶࠫᣰ"),
  bstack11l11ll_opy_ (u"ࠨࡥࡤࡲࡦࡸࡹࠨᣱ"),
  bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪᣲ"),
  bstack11l11ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᣳ"),
  bstack11l11ll_opy_ (u"ࠫ࡮࡫ࠧᣴ"),
  bstack11l11ll_opy_ (u"ࠬ࡫ࡤࡨࡧࠪᣵ"),
  bstack11l11ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭᣶"),
  bstack11l11ll_opy_ (u"ࠧࡲࡷࡨࡹࡪ࠭᣷"),
  bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ᣸"),
  bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࡙ࡴࡰࡴࡨࡇࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠪ᣹"),
  bstack11l11ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡆࡥࡲ࡫ࡲࡢࡋࡰࡥ࡬࡫ࡉ࡯࡬ࡨࡧࡹ࡯࡯࡯ࠩ᣺"),
  bstack11l11ll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡇࡻࡧࡱࡻࡤࡦࡊࡲࡷࡹࡹࠧ᣻"),
  bstack11l11ll_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࡌࡲࡨࡲࡵࡥࡧࡋࡳࡸࡺࡳࠨ᣼"),
  bstack11l11ll_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࠪ᣽"),
  bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡩࡷࡼࡥࡅࡧࡹ࡭ࡨ࡫ࠧ᣾"),
  bstack11l11ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ᣿"),
  bstack11l11ll_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫᤀ"),
  bstack11l11ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡓࡥࡸࡹࡣࡰࡦࡨࠫᤁ"),
  bstack11l11ll_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡍࡴࡹࡄࡦࡸ࡬ࡧࡪ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧᤂ"),
  bstack11l11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡻࡤࡪࡱࡌࡲ࡯࡫ࡣࡵ࡫ࡲࡲࠬᤃ"),
  bstack11l11ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡇࡰࡱ࡮ࡨࡔࡦࡿࠧᤄ"),
  bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᤅ"),
  bstack11l11ll_opy_ (u"ࠨࡹࡧ࡭ࡴ࡙ࡥࡳࡸ࡬ࡧࡪ࠭ᤆ"),
  bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᤇ"),
  bstack11l11ll_opy_ (u"ࠪࡴࡷ࡫ࡶࡦࡰࡷࡇࡷࡵࡳࡴࡕ࡬ࡸࡪ࡚ࡲࡢࡥ࡮࡭ࡳ࡭ࠧᤈ"),
  bstack11l11ll_opy_ (u"ࠫ࡭࡯ࡧࡩࡅࡲࡲࡹࡸࡡࡴࡶࠪᤉ"),
  bstack11l11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡕࡸࡥࡧࡧࡵࡩࡳࡩࡥࡴࠩᤊ"),
  bstack11l11ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩᤋ"),
  bstack11l11ll_opy_ (u"ࠧࡴ࡫ࡰࡓࡵࡺࡩࡰࡰࡶࠫᤌ"),
  bstack11l11ll_opy_ (u"ࠨࡴࡨࡱࡴࡼࡥࡊࡑࡖࡅࡵࡶࡓࡦࡶࡷ࡭ࡳ࡭ࡳࡍࡱࡦࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᤍ"),
  bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫᤎ"),
  bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᤏ"),
  bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᤐ"),
  bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᤑ"),
  bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᤒ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡣࡪࡩࡑࡵࡡࡥࡕࡷࡶࡦࡺࡥࡨࡻࠪᤓ"),
  bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧᤔ"),
  bstack11l11ll_opy_ (u"ࠩࡷ࡭ࡲ࡫࡯ࡶࡶࡶࠫᤕ"),
  bstack11l11ll_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ᤖ")
]
bstack11llll11l_opy_ = {
  bstack11l11ll_opy_ (u"ࠫࡻ࠭ᤗ"): bstack11l11ll_opy_ (u"ࠬࡼࠧᤘ"),
  bstack11l11ll_opy_ (u"࠭ࡦࠨᤙ"): bstack11l11ll_opy_ (u"ࠧࡧࠩᤚ"),
  bstack11l11ll_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࠧᤛ"): bstack11l11ll_opy_ (u"ࠩࡩࡳࡷࡩࡥࠨᤜ"),
  bstack11l11ll_opy_ (u"ࠪࡳࡳࡲࡹࡢࡷࡷࡳࡲࡧࡴࡦࠩᤝ"): bstack11l11ll_opy_ (u"ࠫࡴࡴ࡬ࡺࡃࡸࡸࡴࡳࡡࡵࡧࠪᤞ"),
  bstack11l11ll_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࡰࡴࡩࡡ࡭ࠩ᤟"): bstack11l11ll_opy_ (u"࠭ࡦࡰࡴࡦࡩࡱࡵࡣࡢ࡮ࠪᤠ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡮࡯ࡴࡶࠪᤡ"): bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᤢ"),
  bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡱࡱࡵࡸࠬᤣ"): bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᤤ"),
  bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡸࡷࡪࡸࠧᤥ"): bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᤦ"),
  bstack11l11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩᤧ"): bstack11l11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪᤨ"),
  bstack11l11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽ࡭ࡵࡳࡵࠩᤩ"): bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᤪ"),
  bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡰࡰࡴࡷࠫᤫ"): bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡱࡵࡸࠬ᤬"),
  bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭᤭"): bstack11l11ll_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ᤮"),
  bstack11l11ll_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩ᤯"): bstack11l11ll_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᤰ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶࡡࡴࡵࠪᤱ"): bstack11l11ll_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬᤲ"),
  bstack11l11ll_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭ᤳ"): bstack11l11ll_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᤴ"),
  bstack11l11ll_opy_ (u"࠭ࡢࡪࡰࡤࡶࡾࡶࡡࡵࡪࠪᤵ"): bstack11l11ll_opy_ (u"ࠧࡣ࡫ࡱࡥࡷࡿࡰࡢࡶ࡫ࠫᤶ"),
  bstack11l11ll_opy_ (u"ࠨࡲࡤࡧ࡫࡯࡬ࡦࠩᤷ"): bstack11l11ll_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬᤸ"),
  bstack11l11ll_opy_ (u"ࠪࡴࡦࡩ࠭ࡧ࡫࡯ࡩ᤹ࠬ"): bstack11l11ll_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ᤺"),
  bstack11l11ll_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ᤻"): bstack11l11ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩ᤼"),
  bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡪࡪ࡮ࡲࡥࠨ᤽"): bstack11l11ll_opy_ (u"ࠨ࡮ࡲ࡫࡫࡯࡬ࡦࠩ᤾"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᤿"): bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᥀"),
  bstack11l11ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷ࠭᥁"): bstack11l11ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡰࡦࡣࡷࡩࡷ࠭᥂")
}
bstack11l1l111l11_opy_ = bstack11l11ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡨ࡫ࡷ࡬ࡺࡨ࠮ࡤࡱࡰ࠳ࡵ࡫ࡲࡤࡻ࠲ࡧࡱ࡯࠯ࡳࡧ࡯ࡩࡦࡹࡥࡴ࠱࡯ࡥࡹ࡫ࡳࡵ࠱ࡧࡳࡼࡴ࡬ࡰࡣࡧࠦ᥃")
bstack11l1l11l11l_opy_ = bstack11l11ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠯ࡩࡧࡤࡰࡹ࡮ࡣࡩࡧࡦ࡯ࠧ᥄")
bstack1l111111ll_opy_ = bstack11l11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡨࡨࡸ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡶࡩࡳࡪ࡟ࡴࡦ࡮ࡣࡪࡼࡥ࡯ࡶࡶࠦ᥅")
bstack11l11l1lll_opy_ = bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡻࡩ࠵ࡨࡶࡤࠪ᥆")
bstack1lll1111ll_opy_ = bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧ࠭᥇")
bstack1l1ll11l11_opy_ = bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡴࡥࡹࡶࡢ࡬ࡺࡨࡳࠨ᥈")
bstack1l1l11lll_opy_ = {
  bstack11l11ll_opy_ (u"ࠬࡪࡥࡧࡣࡸࡰࡹ࠭᥉"): bstack11l11ll_opy_ (u"࠭ࡨࡶࡤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭᥊"),
  bstack11l11ll_opy_ (u"ࠧࡶࡵ࠰ࡩࡦࡹࡴࠨ᥋"): bstack11l11ll_opy_ (u"ࠨࡪࡸࡦ࠲ࡻࡳࡦ࠯ࡲࡲࡱࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ᥌"),
  bstack11l11ll_opy_ (u"ࠩࡸࡷࠬ᥍"): bstack11l11ll_opy_ (u"ࠪ࡬ࡺࡨ࠭ࡶࡵ࠰ࡳࡳࡲࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ᥎"),
  bstack11l11ll_opy_ (u"ࠫࡪࡻࠧ᥏"): bstack11l11ll_opy_ (u"ࠬ࡮ࡵࡣ࠯ࡨࡹ࠲ࡵ࡮࡭ࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᥐ"),
  bstack11l11ll_opy_ (u"࠭ࡩ࡯ࠩᥑ"): bstack11l11ll_opy_ (u"ࠧࡩࡷࡥ࠱ࡦࡶࡳ࠮ࡱࡱࡰࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᥒ"),
  bstack11l11ll_opy_ (u"ࠨࡣࡸࠫᥓ"): bstack11l11ll_opy_ (u"ࠩ࡫ࡹࡧ࠳ࡡࡱࡵࡨ࠱ࡴࡴ࡬ࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᥔ")
}
bstack11l1l11lll1_opy_ = {
  bstack11l11ll_opy_ (u"ࠪࡧࡷ࡯ࡴࡪࡥࡤࡰࠬᥕ"): 50,
  bstack11l11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᥖ"): 40,
  bstack11l11ll_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ᥗ"): 30,
  bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᥘ"): 20,
  bstack11l11ll_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᥙ"): 10
}
bstack111ll1l11l_opy_ = bstack11l1l11lll1_opy_[bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᥚ")]
bstack1111ll1111_opy_ = bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᥛ")
bstack1111l1l11_opy_ = bstack11l11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᥜ")
bstack1l1111l1l_opy_ = bstack11l11ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᥝ")
bstack111ll11lll_opy_ = bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᥞ")
bstack111ll1ll_opy_ = bstack11l11ll_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺࠠࡢࡰࡧࠤࡵࡿࡴࡦࡵࡷ࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡰࡢࡥ࡮ࡥ࡬࡫ࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡲࡼࡸࡪࡹࡴ࠮ࡵࡨࡰࡪࡴࡩࡶ࡯ࡣࠫᥟ")
bstack11l11ll11l1_opy_ = [bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᥠ"), bstack11l11ll_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᥡ")]
bstack11l11l11lll_opy_ = [bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᥢ"), bstack11l11ll_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᥣ")]
bstack1lll1ll111_opy_ = re.compile(bstack11l11ll_opy_ (u"ࠫࡣࡡ࡜࡝ࡹ࠰ࡡ࠰ࡀ࠮ࠫࠦࠪᥤ"))
bstack11111ll1l_opy_ = [
  bstack11l11ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡐࡤࡱࡪ࠭ᥥ"),
  bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᥦ"),
  bstack11l11ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᥧ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡨࡻࡈࡵ࡭࡮ࡣࡱࡨ࡙࡯࡭ࡦࡱࡸࡸࠬᥨ"),
  bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࠭ᥩ"),
  bstack11l11ll_opy_ (u"ࠪࡹࡩ࡯ࡤࠨᥪ"),
  bstack11l11ll_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ᥫ"),
  bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡩࠬᥬ"),
  bstack11l11ll_opy_ (u"࠭࡯ࡳ࡫ࡨࡲࡹࡧࡴࡪࡱࡱࠫᥭ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳ࡜࡫ࡢࡷ࡫ࡨࡻࠬ᥮"),
  bstack11l11ll_opy_ (u"ࠨࡰࡲࡖࡪࡹࡥࡵࠩ᥯"), bstack11l11ll_opy_ (u"ࠩࡩࡹࡱࡲࡒࡦࡵࡨࡸࠬᥰ"),
  bstack11l11ll_opy_ (u"ࠪࡧࡱ࡫ࡡࡳࡕࡼࡷࡹ࡫࡭ࡇ࡫࡯ࡩࡸ࠭ᥱ"),
  bstack11l11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡗ࡭ࡲ࡯࡮ࡨࡵࠪᥲ"),
  bstack11l11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࡎࡲ࡫࡬࡯࡮ࡨࠩᥳ"),
  bstack11l11ll_opy_ (u"࠭࡯ࡵࡪࡨࡶࡆࡶࡰࡴࠩᥴ"),
  bstack11l11ll_opy_ (u"ࠧࡱࡴ࡬ࡲࡹࡖࡡࡨࡧࡖࡳࡺࡸࡣࡦࡑࡱࡊ࡮ࡴࡤࡇࡣ࡬ࡰࡺࡸࡥࠨ᥵"),
  bstack11l11ll_opy_ (u"ࠨࡣࡳࡴࡆࡩࡴࡪࡸ࡬ࡸࡾ࠭᥶"), bstack11l11ll_opy_ (u"ࠩࡤࡴࡵࡖࡡࡤ࡭ࡤ࡫ࡪ࠭᥷"), bstack11l11ll_opy_ (u"ࠪࡥࡵࡶࡗࡢ࡫ࡷࡅࡨࡺࡩࡷ࡫ࡷࡽࠬ᥸"), bstack11l11ll_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡕࡧࡣ࡬ࡣࡪࡩࠬ᥹"), bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡊࡵࡳࡣࡷ࡭ࡴࡴࠧ᥺"),
  bstack11l11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫ᥻"),
  bstack11l11ll_opy_ (u"ࠧࡢ࡮࡯ࡳࡼ࡚ࡥࡴࡶࡓࡥࡨࡱࡡࡨࡧࡶࠫ᥼"),
  bstack11l11ll_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡅࡲࡺࡪࡸࡡࡨࡧࠪ᥽"), bstack11l11ll_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡆࡳࡻ࡫ࡲࡢࡩࡨࡉࡳࡪࡉ࡯ࡶࡨࡲࡹ࠭᥾"),
  bstack11l11ll_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡈࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ᥿"),
  bstack11l11ll_opy_ (u"ࠫࡦࡪࡢࡑࡱࡵࡸࠬᦀ"),
  bstack11l11ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡊࡥࡷ࡫ࡦࡩࡘࡵࡣ࡬ࡧࡷࠫᦁ"),
  bstack11l11ll_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡉ࡯ࡵࡷࡥࡱࡲࡔࡪ࡯ࡨࡳࡺࡺࠧᦂ"),
  bstack11l11ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡊࡰࡶࡸࡦࡲ࡬ࡑࡣࡷ࡬ࠬᦃ"),
  bstack11l11ll_opy_ (u"ࠨࡣࡹࡨࠬᦄ"), bstack11l11ll_opy_ (u"ࠩࡤࡺࡩࡒࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬᦅ"), bstack11l11ll_opy_ (u"ࠪࡥࡻࡪࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬᦆ"), bstack11l11ll_opy_ (u"ࠫࡦࡼࡤࡂࡴࡪࡷࠬᦇ"),
  bstack11l11ll_opy_ (u"ࠬࡻࡳࡦࡍࡨࡽࡸࡺ࡯ࡳࡧࠪᦈ"), bstack11l11ll_opy_ (u"࠭࡫ࡦࡻࡶࡸࡴࡸࡥࡑࡣࡷ࡬ࠬᦉ"), bstack11l11ll_opy_ (u"ࠧ࡬ࡧࡼࡷࡹࡵࡲࡦࡒࡤࡷࡸࡽ࡯ࡳࡦࠪᦊ"),
  bstack11l11ll_opy_ (u"ࠨ࡭ࡨࡽࡆࡲࡩࡢࡵࠪᦋ"), bstack11l11ll_opy_ (u"ࠩ࡮ࡩࡾࡖࡡࡴࡵࡺࡳࡷࡪࠧᦌ"),
  bstack11l11ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࠬᦍ"), bstack11l11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡄࡶ࡬ࡹࠧᦎ"), bstack11l11ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࡄࡪࡴࠪᦏ"), bstack11l11ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡈ࡮ࡲࡰ࡯ࡨࡑࡦࡶࡰࡪࡰࡪࡊ࡮ࡲࡥࠨᦐ"), bstack11l11ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷ࡛ࡳࡦࡕࡼࡷࡹ࡫࡭ࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࠫᦑ"),
  bstack11l11ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡐࡰࡴࡷࠫᦒ"), bstack11l11ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡑࡱࡵࡸࡸ࠭ᦓ"),
  bstack11l11ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡆ࡬ࡷࡦࡨ࡬ࡦࡄࡸ࡭ࡱࡪࡃࡩࡧࡦ࡯ࠬᦔ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࡖ࡬ࡱࡪࡵࡵࡵࠩᦕ"),
  bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡵࡧࡱࡸࡆࡩࡴࡪࡱࡱࠫᦖ"), bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡉࡡࡵࡧࡪࡳࡷࡿࠧᦗ"), bstack11l11ll_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡆ࡭ࡣࡪࡷࠬᦘ"), bstack11l11ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࡌࡲࡹ࡫࡮ࡵࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᦙ"),
  bstack11l11ll_opy_ (u"ࠩࡧࡳࡳࡺࡓࡵࡱࡳࡅࡵࡶࡏ࡯ࡔࡨࡷࡪࡺࠧᦚ"),
  bstack11l11ll_opy_ (u"ࠪࡹࡳ࡯ࡣࡰࡦࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬᦛ"), bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡦࡶࡎࡩࡾࡨ࡯ࡢࡴࡧࠫᦜ"),
  bstack11l11ll_opy_ (u"ࠬࡴ࡯ࡔ࡫ࡪࡲࠬᦝ"),
  bstack11l11ll_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࡛࡮ࡪ࡯ࡳࡳࡷࡺࡡ࡯ࡶ࡙࡭ࡪࡽࡳࠨᦞ"),
  bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡰࡧࡶࡴ࡯ࡤࡘࡣࡷࡧ࡭࡫ࡲࡴࠩᦟ"),
  bstack11l11ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᦠ"),
  bstack11l11ll_opy_ (u"ࠩࡵࡩࡨࡸࡥࡢࡶࡨࡇ࡭ࡸ࡯࡮ࡧࡇࡶ࡮ࡼࡥࡳࡕࡨࡷࡸ࡯࡯࡯ࡵࠪᦡ"),
  bstack11l11ll_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧ࡚ࡩࡧ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩᦢ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡘࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡑࡣࡷ࡬ࠬᦣ"),
  bstack11l11ll_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰ࡙ࡰࡦࡧࡧࠫᦤ"),
  bstack11l11ll_opy_ (u"࠭ࡧࡱࡵࡈࡲࡦࡨ࡬ࡦࡦࠪᦥ"),
  bstack11l11ll_opy_ (u"ࠧࡪࡵࡋࡩࡦࡪ࡬ࡦࡵࡶࠫᦦ"),
  bstack11l11ll_opy_ (u"ࠨࡣࡧࡦࡊࡾࡥࡤࡖ࡬ࡱࡪࡵࡵࡵࠩᦧ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࡕࡦࡶ࡮ࡶࡴࠨᦨ"),
  bstack11l11ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡅࡧࡹ࡭ࡨ࡫ࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡣࡷ࡭ࡴࡴࠧᦩ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰࡉࡵࡥࡳࡺࡐࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠫᦪ"),
  bstack11l11ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡔࡡࡵࡷࡵࡥࡱࡕࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᦫ"),
  bstack11l11ll_opy_ (u"࠭ࡳࡺࡵࡷࡩࡲࡖ࡯ࡳࡶࠪ᦬"),
  bstack11l11ll_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡁࡥࡤࡋࡳࡸࡺࠧ᦭"),
  bstack11l11ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡛࡮࡭ࡱࡦ࡯ࠬ᦮"), bstack11l11ll_opy_ (u"ࠩࡸࡲࡱࡵࡣ࡬ࡖࡼࡴࡪ࠭᦯"), bstack11l11ll_opy_ (u"ࠪࡹࡳࡲ࡯ࡤ࡭ࡎࡩࡾ࠭ᦰ"),
  bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰࡎࡤࡹࡳࡩࡨࠨᦱ"),
  bstack11l11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡏࡳ࡬ࡩࡡࡵࡅࡤࡴࡹࡻࡲࡦࠩᦲ"),
  bstack11l11ll_opy_ (u"࠭ࡵ࡯࡫ࡱࡷࡹࡧ࡬࡭ࡑࡷ࡬ࡪࡸࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨᦳ"),
  bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡘ࡫ࡱࡨࡴࡽࡁ࡯࡫ࡰࡥࡹ࡯࡯࡯ࠩᦴ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡔࡰࡱ࡯ࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᦵ"),
  bstack11l11ll_opy_ (u"ࠩࡨࡲ࡫ࡵࡲࡤࡧࡄࡴࡵࡏ࡮ࡴࡶࡤࡰࡱ࠭ᦶ"),
  bstack11l11ll_opy_ (u"ࠪࡩࡳࡹࡵࡳࡧ࡚ࡩࡧࡼࡩࡦࡹࡶࡌࡦࡼࡥࡑࡣࡪࡩࡸ࠭ᦷ"), bstack11l11ll_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡶࡵࡱࡲࡰࡸࡖ࡯ࡳࡶࠪᦸ"), bstack11l11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩ࡜࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡴࡢ࡫࡯ࡷࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᦹ"),
  bstack11l11ll_opy_ (u"࠭ࡲࡦ࡯ࡲࡸࡪࡇࡰࡱࡵࡆࡥࡨ࡮ࡥࡍ࡫ࡰ࡭ࡹ࠭ᦺ"),
  bstack11l11ll_opy_ (u"ࠧࡤࡣ࡯ࡩࡳࡪࡡࡳࡈࡲࡶࡲࡧࡴࠨᦻ"),
  bstack11l11ll_opy_ (u"ࠨࡤࡸࡲࡩࡲࡥࡊࡦࠪᦼ"),
  bstack11l11ll_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩᦽ"),
  bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࡘ࡫ࡲࡷ࡫ࡦࡩࡸࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ᦾ"), bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࡙ࡥࡳࡸ࡬ࡧࡪࡹࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡦࡦࠪᦿ"),
  bstack11l11ll_opy_ (u"ࠬࡧࡵࡵࡱࡄࡧࡨ࡫ࡰࡵࡃ࡯ࡩࡷࡺࡳࠨᧀ"), bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡈ࡮ࡹ࡭ࡪࡵࡶࡅࡱ࡫ࡲࡵࡵࠪᧁ"),
  bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡶࡐ࡮ࡨࠧᧂ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡘࡧࡥࡘࡦࡶࠧᧃ"),
  bstack11l11ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡋࡱ࡭ࡹ࡯ࡡ࡭ࡗࡵࡰࠬᧄ"), bstack11l11ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡄࡰࡱࡵࡷࡑࡱࡳࡹࡵࡹࠧᧅ"), bstack11l11ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡍ࡬ࡴ࡯ࡳࡧࡉࡶࡦࡻࡤࡘࡣࡵࡲ࡮ࡴࡧࠨᧆ"), bstack11l11ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡔࡶࡥ࡯ࡎ࡬ࡲࡰࡹࡉ࡯ࡄࡤࡧࡰ࡭ࡲࡰࡷࡱࡨࠬᧇ"),
  bstack11l11ll_opy_ (u"࠭࡫ࡦࡧࡳࡏࡪࡿࡃࡩࡣ࡬ࡲࡸ࠭ᧈ"),
  bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡯ࡺࡢࡤ࡯ࡩࡘࡺࡲࡪࡰࡪࡷࡉ࡯ࡲࠨᧉ"),
  bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡨ࡫ࡳࡴࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᧊"),
  bstack11l11ll_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡲࡌࡧࡼࡈࡪࡲࡡࡺࠩ᧋"),
  bstack11l11ll_opy_ (u"ࠪࡷ࡭ࡵࡷࡊࡑࡖࡐࡴ࡭ࠧ᧌"),
  bstack11l11ll_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭᧍"),
  bstack11l11ll_opy_ (u"ࠬࡽࡥࡣ࡭࡬ࡸࡗ࡫ࡳࡱࡱࡱࡷࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭᧎"), bstack11l11ll_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶ࡚ࡥ࡮ࡺࡔࡪ࡯ࡨࡳࡺࡺࠧ᧏"),
  bstack11l11ll_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࠪ᧐"),
  bstack11l11ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡵࡼࡲࡨࡋࡸࡦࡥࡸࡸࡪࡌࡲࡰ࡯ࡋࡸࡹࡶࡳࠨ᧑"),
  bstack11l11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡆࡥࡵࡺࡵࡳࡧࠪ᧒"),
  bstack11l11ll_opy_ (u"ࠪࡻࡪࡨ࡫ࡪࡶࡇࡩࡧࡻࡧࡑࡴࡲࡼࡾࡖ࡯ࡳࡶࠪ᧓"),
  bstack11l11ll_opy_ (u"ࠫ࡫ࡻ࡬࡭ࡅࡲࡲࡹ࡫ࡸࡵࡎ࡬ࡷࡹ࠭᧔"),
  bstack11l11ll_opy_ (u"ࠬࡽࡡࡪࡶࡉࡳࡷࡇࡰࡱࡕࡦࡶ࡮ࡶࡴࠨ᧕"),
  bstack11l11ll_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࡃࡰࡰࡱࡩࡨࡺࡒࡦࡶࡵ࡭ࡪࡹࠧ᧖"),
  bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࡒࡦࡳࡥࠨ᧗"),
  bstack11l11ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡕࡏࡇࡪࡸࡴࠨ᧘"),
  bstack11l11ll_opy_ (u"ࠩࡷࡥࡵ࡝ࡩࡵࡪࡖ࡬ࡴࡸࡴࡑࡴࡨࡷࡸࡊࡵࡳࡣࡷ࡭ࡴࡴࠧ᧙"),
  bstack11l11ll_opy_ (u"ࠪࡷࡨࡧ࡬ࡦࡈࡤࡧࡹࡵࡲࠨ᧚"),
  bstack11l11ll_opy_ (u"ࠫࡼࡪࡡࡍࡱࡦࡥࡱࡖ࡯ࡳࡶࠪ᧛"),
  bstack11l11ll_opy_ (u"ࠬࡹࡨࡰࡹ࡛ࡧࡴࡪࡥࡍࡱࡪࠫ᧜"),
  bstack11l11ll_opy_ (u"࠭ࡩࡰࡵࡌࡲࡸࡺࡡ࡭࡮ࡓࡥࡺࡹࡥࠨ᧝"),
  bstack11l11ll_opy_ (u"ࠧࡹࡥࡲࡨࡪࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠩ᧞"),
  bstack11l11ll_opy_ (u"ࠨ࡭ࡨࡽࡨ࡮ࡡࡪࡰࡓࡥࡸࡹࡷࡰࡴࡧࠫ᧟"),
  bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡖࡲࡦࡤࡸ࡭ࡱࡺࡗࡅࡃࠪ᧠"),
  bstack11l11ll_opy_ (u"ࠪࡴࡷ࡫ࡶࡦࡰࡷ࡛ࡉࡇࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠫ᧡"),
  bstack11l11ll_opy_ (u"ࠫࡼ࡫ࡢࡅࡴ࡬ࡺࡪࡸࡁࡨࡧࡱࡸ࡚ࡸ࡬ࠨ᧢"),
  bstack11l11ll_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡶ࡫ࠫ᧣"),
  bstack11l11ll_opy_ (u"࠭ࡵࡴࡧࡑࡩࡼ࡝ࡄࡂࠩ᧤"),
  bstack11l11ll_opy_ (u"ࠧࡸࡦࡤࡐࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᧥"), bstack11l11ll_opy_ (u"ࠨࡹࡧࡥࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࡕ࡫ࡰࡩࡴࡻࡴࠨ᧦"),
  bstack11l11ll_opy_ (u"ࠩࡻࡧࡴࡪࡥࡐࡴࡪࡍࡩ࠭᧧"), bstack11l11ll_opy_ (u"ࠪࡼࡨࡵࡤࡦࡕ࡬࡫ࡳ࡯࡮ࡨࡋࡧࠫ᧨"),
  bstack11l11ll_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨ࡜ࡊࡁࡃࡷࡱࡨࡱ࡫ࡉࡥࠩ᧩"),
  bstack11l11ll_opy_ (u"ࠬࡸࡥࡴࡧࡷࡓࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡴࡷࡓࡳࡲࡹࠨ᧪"),
  bstack11l11ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡔࡪ࡯ࡨࡳࡺࡺࡳࠨ᧫"),
  bstack11l11ll_opy_ (u"ࠧࡸࡦࡤࡗࡹࡧࡲࡵࡷࡳࡖࡪࡺࡲࡪࡧࡶࠫ᧬"), bstack11l11ll_opy_ (u"ࠨࡹࡧࡥࡘࡺࡡࡳࡶࡸࡴࡗ࡫ࡴࡳࡻࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠫ᧭"),
  bstack11l11ll_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࡋࡥࡷࡪࡷࡢࡴࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬ᧮"),
  bstack11l11ll_opy_ (u"ࠪࡱࡦࡾࡔࡺࡲ࡬ࡲ࡬ࡌࡲࡦࡳࡸࡩࡳࡩࡹࠨ᧯"),
  bstack11l11ll_opy_ (u"ࠫࡸ࡯࡭ࡱ࡮ࡨࡍࡸ࡜ࡩࡴ࡫ࡥࡰࡪࡉࡨࡦࡥ࡮ࠫ᧰"),
  bstack11l11ll_opy_ (u"ࠬࡻࡳࡦࡅࡤࡶࡹ࡮ࡡࡨࡧࡖࡷࡱ࠭᧱"),
  bstack11l11ll_opy_ (u"࠭ࡳࡩࡱࡸࡰࡩ࡛ࡳࡦࡕ࡬ࡲ࡬ࡲࡥࡵࡱࡱࡘࡪࡹࡴࡎࡣࡱࡥ࡬࡫ࡲࠨ᧲"),
  bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹࡏࡗࡅࡒࠪ᧳"),
  bstack11l11ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡔࡰࡷࡦ࡬ࡎࡪࡅ࡯ࡴࡲࡰࡱ࠭᧴"),
  bstack11l11ll_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࡊ࡬ࡨࡩ࡫࡮ࡂࡲ࡬ࡔࡴࡲࡩࡤࡻࡈࡶࡷࡵࡲࠨ᧵"),
  bstack11l11ll_opy_ (u"ࠪࡱࡴࡩ࡫ࡍࡱࡦࡥࡹ࡯࡯࡯ࡃࡳࡴࠬ᧶"),
  bstack11l11ll_opy_ (u"ࠫࡱࡵࡧࡤࡣࡷࡊࡴࡸ࡭ࡢࡶࠪ᧷"), bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࡥࡤࡸࡋ࡯࡬ࡵࡧࡵࡗࡵ࡫ࡣࡴࠩ᧸"),
  bstack11l11ll_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡉ࡫࡬ࡢࡻࡄࡨࡧ࠭᧹"),
  bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡊࡦࡏࡳࡨࡧࡴࡰࡴࡄࡹࡹࡵࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠪ᧺")
]
bstack11ll111111_opy_ = bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡶࡲ࡯ࡳࡦࡪࠧ᧻")
bstack11ll1ll1l_opy_ = [bstack11l11ll_opy_ (u"ࠩ࠱ࡥࡵࡱࠧ᧼"), bstack11l11ll_opy_ (u"ࠪ࠲ࡦࡧࡢࠨ᧽"), bstack11l11ll_opy_ (u"ࠫ࠳࡯ࡰࡢࠩ᧾")]
bstack1l1lll1l1_opy_ = [bstack11l11ll_opy_ (u"ࠬ࡯ࡤࠨ᧿"), bstack11l11ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫᨀ"), bstack11l11ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪᨁ"), bstack11l11ll_opy_ (u"ࠨࡵ࡫ࡥࡷ࡫ࡡࡣ࡮ࡨࡣ࡮ࡪࠧᨂ")]
bstack1ll1111111_opy_ = {
  bstack11l11ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᨃ"): bstack11l11ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᨄ"),
  bstack11l11ll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬᨅ"): bstack11l11ll_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᨆ"),
  bstack11l11ll_opy_ (u"࠭ࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫᨇ"): bstack11l11ll_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᨈ"),
  bstack11l11ll_opy_ (u"ࠨ࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᨉ"): bstack11l11ll_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᨊ"),
  bstack11l11ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡒࡴࡹ࡯࡯࡯ࡵࠪᨋ"): bstack11l11ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬᨌ")
}
bstack11l1ll1ll1_opy_ = [
  bstack11l11ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᨍ"),
  bstack11l11ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᨎ"),
  bstack11l11ll_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᨏ"),
  bstack11l11ll_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᨐ"),
  bstack11l11ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪᨑ"),
]
bstack1111lllll_opy_ = bstack1l111ll1l_opy_ + bstack11l1l11l111_opy_ + bstack11111ll1l_opy_
bstack1ll11l1lll_opy_ = [
  bstack11l11ll_opy_ (u"ࠪࡢࡱࡵࡣࡢ࡮࡫ࡳࡸࡺࠤࠨᨒ"),
  bstack11l11ll_opy_ (u"ࠫࡣࡨࡳ࠮࡮ࡲࡧࡦࡲ࠮ࡤࡱࡰࠨࠬᨓ"),
  bstack11l11ll_opy_ (u"ࠬࡤ࠱࠳࠹࠱ࠫᨔ"),
  bstack11l11ll_opy_ (u"࠭࡞࠲࠲࠱ࠫᨕ"),
  bstack11l11ll_opy_ (u"ࠧ࡟࠳࠺࠶࠳࠷࡛࠷࠯࠼ࡡ࠳࠭ᨖ"),
  bstack11l11ll_opy_ (u"ࠨࡠ࠴࠻࠷࠴࠲࡜࠲࠰࠽ࡢ࠴ࠧᨗ"),
  bstack11l11ll_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠴࡝࠳࠱࠶ࡣ࠮ࠨᨘ"),
  bstack11l11ll_opy_ (u"ࠪࡢ࠶࠿࠲࠯࠳࠹࠼࠳࠭ᨙ")
]
bstack11l11ll1l11_opy_ = bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᨚ")
bstack11l11111l1_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠱ࡹ࠵࠴࡫ࡶࡦࡰࡷࠫᨛ")
bstack1111lll111_opy_ = [ bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ᨜") ]
bstack11llll1111_opy_ = [ bstack11l11ll_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭᨝") ]
bstack1111111l1_opy_ = [bstack11l11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ᨞")]
bstack1llll1l1ll_opy_ = [ bstack11l11ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᨟") ]
bstack11lllll1l1_opy_ = bstack11l11ll_opy_ (u"ࠪࡗࡉࡑࡓࡦࡶࡸࡴࠬᨠ")
bstack1l11111111_opy_ = bstack11l11ll_opy_ (u"ࠫࡘࡊࡋࡕࡧࡶࡸࡆࡺࡴࡦ࡯ࡳࡸࡪࡪࠧᨡ")
bstack11111111l_opy_ = bstack11l11ll_opy_ (u"࡙ࠬࡄࡌࡖࡨࡷࡹ࡙ࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠩᨢ")
bstack1l1ll11111_opy_ = bstack11l11ll_opy_ (u"࠭࠴࠯࠲࠱࠴ࠬᨣ")
bstack1ll11111ll_opy_ = [
  bstack11l11ll_opy_ (u"ࠧࡆࡔࡕࡣࡋࡇࡉࡍࡇࡇࠫᨤ"),
  bstack11l11ll_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡉࡎࡇࡇࡣࡔ࡛ࡔࠨᨥ"),
  bstack11l11ll_opy_ (u"ࠩࡈࡖࡗࡥࡂࡍࡑࡆࡏࡊࡊ࡟ࡃ࡛ࡢࡇࡑࡏࡅࡏࡖࠪᨦ"),
  bstack11l11ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡇࡗ࡛ࡔࡘࡋࡠࡅࡋࡅࡓࡍࡅࡅࠩᨧ"),
  bstack11l11ll_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐࡋࡔࡠࡐࡒࡘࡤࡉࡏࡏࡐࡈࡇ࡙ࡋࡄࠨᨨ"),
  bstack11l11ll_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡃࡍࡑࡖࡉࡉ࠭ᨩ"),
  bstack11l11ll_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡓࡇࡖࡉ࡙࠭ᨪ"),
  bstack11l11ll_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡔࡈࡊ࡚࡙ࡅࡅࠩᨫ"),
  bstack11l11ll_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡄࡆࡔࡘࡔࡆࡆࠪᨬ"),
  bstack11l11ll_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᨭ"),
  bstack11l11ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡃࡐࡉࡤࡔࡏࡕࡡࡕࡉࡘࡕࡌࡗࡇࡇࠫᨮ"),
  bstack11l11ll_opy_ (u"ࠫࡊࡘࡒࡠࡃࡇࡈࡗࡋࡓࡔࡡࡌࡒ࡛ࡇࡌࡊࡆࠪᨯ"),
  bstack11l11ll_opy_ (u"ࠬࡋࡒࡓࡡࡄࡈࡉࡘࡅࡔࡕࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨᨰ"),
  bstack11l11ll_opy_ (u"࠭ࡅࡓࡔࡢࡘ࡚ࡔࡎࡆࡎࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᨱ"),
  bstack11l11ll_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫᨲ"),
  bstack11l11ll_opy_ (u"ࠨࡇࡕࡖࡤ࡙ࡏࡄࡍࡖࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨᨳ"),
  bstack11l11ll_opy_ (u"ࠩࡈࡖࡗࡥࡓࡐࡅࡎࡗࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡋࡓࡘ࡚࡟ࡖࡐࡕࡉࡆࡉࡈࡂࡄࡏࡉࠬᨴ"),
  bstack11l11ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡑࡔࡒ࡜࡞ࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᨵ"),
  bstack11l11ll_opy_ (u"ࠫࡊࡘࡒࡠࡐࡄࡑࡊࡥࡎࡐࡖࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࠬᨶ"),
  bstack11l11ll_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡓࡇࡖࡓࡑ࡛ࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᨷ"),
  bstack11l11ll_opy_ (u"࠭ࡅࡓࡔࡢࡑࡆࡔࡄࡂࡖࡒࡖ࡞ࡥࡐࡓࡑ࡛࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᨸ"),
]
bstack111lll1l1_opy_ = bstack11l11ll_opy_ (u"ࠧ࠯࠱ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡣࡵࡸ࡮࡬ࡡࡤࡶࡶ࠳ࠬᨹ")
bstack1l111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠨࢀࠪᨺ")), bstack11l11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᨻ"), bstack11l11ll_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᨼ"))
bstack11l1l11ll11_opy_ = bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳ࡭ࠬᨽ")
bstack11l1l1111ll_opy_ = [ bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᨾ"), bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᨿ"), bstack11l11ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ᩀ"), bstack11l11ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨᩁ")]
bstack111l1l11ll_opy_ = [ bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᩂ"), bstack11l11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩᩃ"), bstack11l11ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪᩄ"), bstack11l11ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬᩅ") ]
bstack1111ll11l_opy_ = [ bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᩆ") ]
bstack11l11llll11_opy_ = [ bstack11l11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᩇ") ]
bstack1ll1l1l1l_opy_ = 360
bstack11ll11l1l1l_opy_ = bstack11l11ll_opy_ (u"ࠣࡣࡳࡴ࠲ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣᩈ")
bstack11l11l11ll1_opy_ = bstack11l11ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳࡮ࡹࡳࡶࡧࡶࠦᩉ")
bstack11l1l1111l1_opy_ = bstack11l11ll_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴࡯ࡳࡴࡷࡨࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾࠨᩊ")
bstack11l1l11llll_opy_ = bstack11l11ll_opy_ (u"ࠦࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡺࡥࡴࡶࡶࠤࡦࡸࡥࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡐࡕࠣࡺࡪࡸࡳࡪࡱࡱࠤࠪࡹࠠࡢࡰࡧࠤࡦࡨ࡯ࡷࡧࠣࡪࡴࡸࠠࡂࡰࡧࡶࡴ࡯ࡤࠡࡦࡨࡺ࡮ࡩࡥࡴ࠰ࠥᩋ")
bstack11l11lll11l_opy_ = bstack11l11ll_opy_ (u"ࠧ࠷࠱࠯࠲ࠥᩌ")
bstack1ll11l11_opy_ = {
  bstack11l11ll_opy_ (u"࠭ࡐࡂࡕࡖࠫᩍ"): bstack11l11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᩎ"),
  bstack11l11ll_opy_ (u"ࠨࡈࡄࡍࡑ࠭ᩏ"): bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᩐ"),
  bstack11l11ll_opy_ (u"ࠪࡗࡐࡏࡐࠨᩑ"): bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᩒ")
}
bstack111ll1l11_opy_ = [
  bstack11l11ll_opy_ (u"ࠧ࡭ࡥࡵࠤᩓ"),
  bstack11l11ll_opy_ (u"ࠨࡧࡰࡄࡤࡧࡰࠨᩔ"),
  bstack11l11ll_opy_ (u"ࠢࡨࡱࡉࡳࡷࡽࡡࡳࡦࠥᩕ"),
  bstack11l11ll_opy_ (u"ࠣࡴࡨࡪࡷ࡫ࡳࡩࠤᩖ"),
  bstack11l11ll_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᩗ"),
  bstack11l11ll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᩘ"),
  bstack11l11ll_opy_ (u"ࠦࡸࡻࡢ࡮࡫ࡷࡉࡱ࡫࡭ࡦࡰࡷࠦᩙ"),
  bstack11l11ll_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤᩚ"),
  bstack11l11ll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤᩛ"),
  bstack11l11ll_opy_ (u"ࠢࡤ࡮ࡨࡥࡷࡋ࡬ࡦ࡯ࡨࡲࡹࠨᩜ"),
  bstack11l11ll_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࡴࠤᩝ"),
  bstack11l11ll_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵࠤᩞ"),
  bstack11l11ll_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࡅࡸࡿ࡮ࡤࡕࡦࡶ࡮ࡶࡴࠣ᩟"),
  bstack11l11ll_opy_ (u"ࠦࡨࡲ࡯ࡴࡧ᩠ࠥ"),
  bstack11l11ll_opy_ (u"ࠧࡷࡵࡪࡶࠥᩡ"),
  bstack11l11ll_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳࡔࡰࡷࡦ࡬ࡆࡩࡴࡪࡱࡱࠦᩢ"),
  bstack11l11ll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡎࡷ࡯ࡸ࡮࡚࡯ࡶࡥ࡫ࠦᩣ"),
  bstack11l11ll_opy_ (u"ࠣࡵ࡫ࡥࡰ࡫ࠢᩤ"),
  bstack11l11ll_opy_ (u"ࠤࡦࡰࡴࡹࡥࡂࡲࡳࠦᩥ")
]
bstack11l11l1l11l_opy_ = [
  bstack11l11ll_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤᩦ"),
  bstack11l11ll_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᩧ"),
  bstack11l11ll_opy_ (u"ࠧࡧࡵࡵࡱࠥᩨ"),
  bstack11l11ll_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨᩩ"),
  bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᩪ")
]
bstack1l1lll1ll_opy_ = {
  bstack11l11ll_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢᩫ"): [bstack11l11ll_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᩬ")],
  bstack11l11ll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᩭ"): [bstack11l11ll_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᩮ")],
  bstack11l11ll_opy_ (u"ࠧࡧࡵࡵࡱࠥᩯ"): [bstack11l11ll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᩰ"), bstack11l11ll_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᩱ"), bstack11l11ll_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᩲ"), bstack11l11ll_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᩳ")],
  bstack11l11ll_opy_ (u"ࠥࡱࡦࡴࡵࡢ࡮ࠥᩴ"): [bstack11l11ll_opy_ (u"ࠦࡲࡧ࡮ࡶࡣ࡯ࠦ᩵")],
  bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ᩶"): [bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣ᩷")],
}
bstack11l11llllll_opy_ = {
  bstack11l11ll_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࡋ࡬ࡦ࡯ࡨࡲࡹࠨ᩸"): bstack11l11ll_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢ᩹"),
  bstack11l11ll_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨ᩺"): bstack11l11ll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢ᩻"),
  bstack11l11ll_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸ࡚࡯ࡆ࡮ࡨࡱࡪࡴࡴࠣ᩼"): bstack11l11ll_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࠢ᩽"),
  bstack11l11ll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤ᩾"): bstack11l11ll_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࠤ᩿"),
  bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ᪀"): bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ᪁")
}
bstack1l1l1l11_opy_ = {
  bstack11l11ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧ᪂"): bstack11l11ll_opy_ (u"ࠫࡘࡻࡩࡵࡧࠣࡗࡪࡺࡵࡱࠩ᪃"),
  bstack11l11ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ᪄"): bstack11l11ll_opy_ (u"࠭ࡓࡶ࡫ࡷࡩ࡚ࠥࡥࡢࡴࡧࡳࡼࡴࠧ᪅"),
  bstack11l11ll_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ᪆"): bstack11l11ll_opy_ (u"ࠨࡖࡨࡷࡹࠦࡓࡦࡶࡸࡴࠬ᪇"),
  bstack11l11ll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭᪈"): bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࠡࡖࡨࡥࡷࡪ࡯ࡸࡰࠪ᪉")
}
bstack11l1l11l1l1_opy_ = 65536
bstack11l11ll1111_opy_ = bstack11l11ll_opy_ (u"ࠫ࠳࠴࠮࡜ࡖࡕ࡙ࡓࡉࡁࡕࡇࡇࡡࠬ᪊")
bstack11l11ll1ll1_opy_ = [
      bstack11l11ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ᪋"), bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ᪌"), bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᪍"), bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᪎"), bstack11l11ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫ᪏"),
      bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭᪐"), bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᪑"), bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭᪒"), bstack11l11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᪓"),
      bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡒࡦࡳࡥࠨ᪔"), bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ᪕"), bstack11l11ll_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬ᪖")
    ]
bstack11l1l11l1ll_opy_= {
  bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᪗"): bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᪘"),
  bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪙"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ᪚"),
  bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᪛"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ᪜"),
  bstack11l11ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᪝"): bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᪞"),
  bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᪟"): bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᪠"),
  bstack11l11ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ᪡"): bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩ᪢"),
  bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᪣"): bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᪤"),
  bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᪥"): bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᪦"),
  bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᪧ"): bstack11l11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ᪨"),
  bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ᪩"): bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭᪪"),
  bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭᪫"): bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᪬"),
  bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠫ᪭"): bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬ᪮"),
  bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᪯"): bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᪰"),
  bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨ᪱"): bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪲"),
  bstack11l11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠬ᪳"): bstack11l11ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭᪴"),
  bstack11l11ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯᪵ࠩ"): bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᪶"),
  bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯᪷ࠩ"): bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ᪸ࠪ"),
  bstack11l11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ᪹࠭"): bstack11l11ll_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹ᪺ࠧ"),
  bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ᪻"): bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ᪼"),
  bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷ᪽ࠬ"): bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭᪾"),
  bstack11l11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨᪿࠫ"): bstack11l11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩᫀࠬ"),
  bstack11l11ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬ᫁"): bstack11l11ll_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭᫂"),
  bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ᫃ࠬ"): bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ᫄࠭"),
  bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᫅"): bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᫆"),
  bstack11l11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭᫇"): bstack11l11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ᫈"),
  bstack11l11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᫉"): bstack11l11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴ᫊ࠩ"),
  bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᫋"): bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᫌ"),
  bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨᫍ"): bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᫎ")
}
bstack11l11lllll1_opy_ = [bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᫏"), bstack11l11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ᫐")]
bstack1l11ll11ll_opy_ = (bstack11l11ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ᫑"),)
bstack11l11lll1l1_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠲ࡺ࠶࠵ࡵࡱࡦࡤࡸࡪࡥࡣ࡭࡫ࠪ᫒")
bstack1ll1111ll_opy_ = bstack11l11ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠰ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠯ࡷ࠳࠲࡫ࡷ࡯ࡤࡴ࠱ࠥ᫓")
bstack111lllll11_opy_ = bstack11l11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪࡶ࡮ࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡦࡹࡨࡣࡱࡤࡶࡩ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࠢ᫔")
bstack1lll1l1111_opy_ = bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠥ᫕")
class EVENTS(Enum):
  bstack11l1l111ll1_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡰ࠳࠴ࡽ࠿ࡶࡲࡪࡰࡷ࠱ࡧࡻࡩ࡭ࡦ࡯࡭ࡳࡱࠧ᫖")
  bstack1llll1llll_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯ࡩࡦࡴࡵࡱࠩ᫗") # final bstack11l11l1l1ll_opy_
  bstack11l11l1ll1l_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡶࡩࡳࡪ࡬ࡰࡩࡶࠫ᫘")
  bstack11llllll11_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᫙") #shift post bstack11l1l111lll_opy_
  bstack111l11ll1_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡰࡳ࡫ࡱࡸ࠲ࡨࡵࡪ࡮ࡧࡰ࡮ࡴ࡫ࠨ᫚") #shift post bstack11l1l111lll_opy_
  bstack11l11l1lll1_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶ࡫ࡹࡧ࠭᫛") #shift
  bstack11l11ll111l_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡰࡦࡴࡦࡽ࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧ᫜") #shift
  bstack1lll111lll_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠾࡭ࡻࡢ࠮࡯ࡤࡲࡦ࡭ࡥ࡮ࡧࡱࡸࠬ᫝")
  bstack1l11111ll1l_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡳࡢࡸࡨ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷࠬ᫞")
  bstack1lll111l11_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡥࡴ࡬ࡺࡪࡸ࠭ࡱࡧࡵࡪࡴࡸ࡭ࡴࡥࡤࡲࠬ᫟")
  bstack11l1l1l111_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡲ࡯ࡤࡣ࡯ࠫ᫠") #shift
  bstack1l1ll1lll_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡥࡵࡶ࠭ࡶࡲ࡯ࡳࡦࡪࠧ᫡") #shift
  bstack11l11l111l_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡤ࡫࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠭᫢")
  bstack1l1l11llll_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡡ࠲࠳ࡼ࠾࡬࡫ࡴ࠮ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠮ࡴࡨࡷࡺࡲࡴࡴ࠯ࡶࡹࡲࡳࡡࡳࡻࠪ᫣") #shift
  bstack1ll11l1ll1_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࠳࠴ࡽ࠿࡭ࡥࡵ࠯ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ࠯ࡵࡩࡸࡻ࡬ࡵࡵࠪ᫤") #shift
  bstack11l11l1l1l1_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿࠧ᫥") #shift
  bstack11llll1ll1l_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ᫦")
  bstack11111ll11l_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡹࡥࡴࡵ࡬ࡳࡳ࠳ࡳࡵࡣࡷࡹࡸ࠭᫧") #shift
  bstack1ll1111lll_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺࠧ᫨")
  bstack11l11lll1ll_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡲࡰࡺࡼ࠱ࡸ࡫ࡴࡶࡲࠪ᫩") #shift
  bstack1ll111111_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡳࡦࡶࡸࡴࠬ᫪")
  bstack11l11lll111_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡳ࡯ࡣࡳࡷ࡭ࡵࡴࠨ᫫") # not bstack11l1l11111l_opy_ in python
  bstack1llll111ll_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲ࠻ࡳࡸ࡭ࡹ࠭᫬") # used in bstack11l11l1llll_opy_
  bstack1l111l1ll1_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡪࡩࡹ࠭᫭") # used in bstack11l11l1llll_opy_
  bstack1ll11l11l1_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽࡬ࡴࡵ࡫ࠨ᫮")
  bstack1l1l11lll1_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠬ᫯")
  bstack11ll1lll1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠬ᫰") #
  bstack1ll1ll1111_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀ࡯࠲࠳ࡼ࠾ࡩࡸࡩࡷࡧࡵ࠱ࡹࡧ࡫ࡦࡕࡦࡶࡪ࡫࡮ࡔࡪࡲࡸࠬ᫱")
  bstack111l1l1lll_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡡࡶࡶࡲ࠱ࡨࡧࡰࡵࡷࡵࡩࠬ᫲")
  bstack11l1lll11l_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡵࡩ࠲ࡺࡥࡴࡶࠪ᫳")
  bstack1l1l1llll_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡳࡸࡺ࠭ࡵࡧࡶࡸࠬ᫴")
  bstack11l1l1llll_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡷ࡫࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᫵") #shift
  bstack1ll1ll11ll_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪ᫶") #shift
  bstack11l11ll1l1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱ࠰ࡧࡦࡶࡴࡶࡴࡨࠫ᫷")
  bstack11l1l1l1111_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻࡫ࡧࡰࡪ࠳ࡴࡪ࡯ࡨࡳࡺࡺࠧ᫸")
  bstack1l11lll1lll_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡸࡺࡡࡳࡶࠪ᫹")
  bstack11l11llll1l_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧ᫺")
  bstack11l11ll1lll_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡣࡩࡧࡦ࡯࠲ࡻࡰࡥࡣࡷࡩࠬ᫻")
  bstack1l11ll1l111_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡰࡰ࠰ࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠭᫼")
  bstack1l1l11l111l_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡱࡱ࠱ࡨࡵ࡮࡯ࡧࡦࡸࠬ᫽")
  bstack1l1l111ll11_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡹࡴࡰࡲࠪ᫾")
  bstack1l11ll111ll_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡳࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࠨ᫿")
  bstack1l11ll11ll1_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱࠫᬀ")
  bstack11l11l1l111_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲࡊࡰ࡬ࡸࠬᬁ")
  bstack11l1l111l1l_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡩ࡭ࡳࡪࡎࡦࡣࡵࡩࡸࡺࡈࡶࡤࠪᬂ")
  bstack1llll1ll111_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡋࡱ࡭ࡹ࠭ᬃ")
  bstack1llllll111l_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡸࡴࠨᬄ")
  bstack1l111l1l1ll_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡈࡵ࡮ࡧ࡫ࡪࠫᬅ")
  bstack11l11ll11ll_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡉ࡯࡯ࡨ࡬࡫ࠬᬆ")
  bstack1l1ll111lll_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࡫ࡖࡩࡱ࡬ࡈࡦࡣ࡯ࡗࡹ࡫ࡰࠨᬇ")
  bstack1l1ll11l111_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࡬ࡗࡪࡲࡦࡉࡧࡤࡰࡌ࡫ࡴࡓࡧࡶࡹࡱࡺࠧᬈ")
  bstack1l11l1ll1ll_opy_ = bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡇࡹࡩࡳࡺࠧᬉ")
  bstack1l11l1l1l1l_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡪࡹࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡆࡸࡨࡲࡹ࠭ᬊ")
  bstack1l111lll1l1_opy_ = bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻࡮ࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࡊࡼࡥ࡯ࡶࠪᬋ")
  bstack11l1l11ll1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡨࡲࡶࡻࡥࡶࡧࡗࡩࡸࡺࡅࡷࡧࡱࡸࠬᬌ")
  bstack1lllll1ll11_opy_ = bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺ࡯ࡱࠩᬍ")
  bstack1l1l1l1ll1l_opy_ = bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡰࡰࡖࡸࡴࡶࠧᬎ")
class STAGE(Enum):
  bstack1l1111l111_opy_ = bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪᬏ")
  END = bstack11l11ll_opy_ (u"ࠬ࡫࡮ࡥࠩᬐ")
  bstack1l1l1l1lll_opy_ = bstack11l11ll_opy_ (u"࠭ࡳࡪࡰࡪࡰࡪ࠭ᬑ")
bstack1ll1ll1l1l_opy_ = {
  bstack11l11ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧᬒ"): bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᬓ"),
  bstack11l11ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭ᬔ"): bstack11l11ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᬕ")
}
PLAYWRIGHT_HUB_URL = bstack11l11ll_opy_ (u"ࠦࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂࠨᬖ")
bstack1l1111l1lll_opy_ = 98
bstack1l1111ll111_opy_ = 100
bstack1lll1ll11_opy_ = {
  bstack11l11ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࠫᬗ"): bstack11l11ll_opy_ (u"࠭࠭࠮ࡴࡨࡶࡺࡴࡳࠨᬘ"),
  bstack11l11ll_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭ᬙ"): bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡶࡪࡸࡵ࡯ࡵ࠰ࡨࡪࡲࡡࡺࠩᬚ"),
  bstack11l11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧᬛ"): 0
}
bstack11ll1ll1ll1_opy_ = bstack11l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᬜ")
bstack11l11l1ll11_opy_ = bstack11l11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡻࡰ࡭ࡱࡤࡨ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣᬝ")
bstack111l11l1l_opy_ = bstack11l11ll_opy_ (u"࡚ࠧࡅࡔࡖࠣࡖࡊࡖࡏࡓࡖࡌࡒࡌࠦࡁࡏࡆࠣࡅࡓࡇࡌ࡚ࡖࡌࡇࡘࠨᬞ")