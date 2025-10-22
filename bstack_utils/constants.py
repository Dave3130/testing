# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
import re
from enum import Enum
bstack1llll1llll_opy_ = {
  bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ៀ"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩេ"),
  bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩែ"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪៃ"),
  bstack111l1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫោ"): bstack111l1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ៅ"),
  bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪំ"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫះ"),
  bstack111l1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪៈ"): bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧ៉"),
  bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ៊"): bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧ់"),
  bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ៌"): bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ៍"),
  bstack111l1l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪ៎"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪ៏"),
  bstack111l1l_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫ័"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧ៑"),
  bstack111l1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ្࠭"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭៓"),
  bstack111l1l_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧ។"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧ៕"),
  bstack111l1l_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫ៖"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫៗ"),
  bstack111l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭៘"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭៙"),
  bstack111l1l_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ៚"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ៛"),
  bstack111l1l_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩៜ"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩ៝"),
  bstack111l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ៞"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ៟"),
  bstack111l1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ០"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ១"),
  bstack111l1l_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ២"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ៣"),
  bstack111l1l_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ៤"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ៥"),
  bstack111l1l_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ៦"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ៧"),
  bstack111l1l_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫ៨"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫ៩"),
  bstack111l1l_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭៪"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭៫"),
  bstack111l1l_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬ៬"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬ៭"),
  bstack111l1l_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩ៮"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩ៯"),
  bstack111l1l_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ៰"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ៱"),
  bstack111l1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ៲"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ៳"),
  bstack111l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ៴"): bstack111l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ៵"),
  bstack111l1l_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭៶"): bstack111l1l_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨ៷"),
  bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ៸"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ៹"),
  bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭៺"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭៻"),
  bstack111l1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ៼"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ៽"),
  bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩ៾"): bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬ៿"),
  bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᠀"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᠁"),
  bstack111l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ᠂"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧ᠃"),
  bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᠄"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᠅"),
  bstack111l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭᠆"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭᠇"),
  bstack111l1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ᠈"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ᠉"),
  bstack111l1l_opy_ (u"ࠨࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬ᠊"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬ᠋"),
  bstack111l1l_opy_ (u"ࠪࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨ᠌"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨ᠍"),
  bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᠎"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᠏"),
  bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ᠐"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ᠑")
}
bstack11l11l1llll_opy_ = [
  bstack111l1l_opy_ (u"ࠩࡲࡷࠬ᠒"),
  bstack111l1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᠓"),
  bstack111l1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᠔"),
  bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᠕"),
  bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ᠖"),
  bstack111l1l_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫ᠗"),
  bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᠘"),
]
bstack1l11111l1_opy_ = {
  bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ᠙"): [bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫ᠚"), bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡐࡄࡑࡊ࠭᠛")],
  bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ᠜"): bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ᠝"),
  bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᠞"): bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠫ᠟"),
  bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᠠ"): bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠨᠡ"),
  bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᠢ"): bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᠣ"),
  bstack111l1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᠤ"): bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡔࡡࡓࡉࡗࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨᠥ"),
  bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᠦ"): bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒࠧᠧ"),
  bstack111l1l_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᠨ"): bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨᠩ"),
  bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩᠪ"): [bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡐࡑࡡࡌࡈࠬᠫ"), bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡑࡒࠪᠬ")],
  bstack111l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᠭ"): bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡕࡇࡏࡤࡒࡏࡈࡎࡈ࡚ࡊࡒࠧᠮ"),
  bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᠯ"): bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᠰ"),
  bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᠱ"): [bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡓࡇ࡙ࡅࡓࡘࡄࡆࡎࡒࡉࡕ࡛ࠪᠲ"), bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧᠳ")],
  bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᠴ"): bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡘࡖࡇࡕࡓࡄࡃࡏࡉࠬᠵ"),
  bstack111l1l_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡊࡔࡖࠨᠶ"): bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡓࡗࡉࡈࡆࡕࡗࡖࡆ࡚ࡉࡐࡐࡢࡗࡒࡇࡒࡕࡡࡖࡉࡑࡋࡃࡕࡋࡒࡒࡤࡌࡅࡂࡖࡘࡖࡊࡥࡂࡓࡃࡑࡇࡍࡋࡓࠨᠷ")
}
bstack1l1lll1l11_opy_ = {
  bstack111l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᠸ"): [bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࡢࡲࡦࡳࡥࠨᠹ"), bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡒࡦࡳࡥࠨᠺ")],
  bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᠻ"): [bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡠ࡭ࡨࡽࠬᠼ"), bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᠽ")],
  bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᠾ"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᠿ"),
  bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᡀ"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᡁ"),
  bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᡂ"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᡃ"),
  bstack111l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᡄ"): [bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡵࡶࠧᡅ"), bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᡆ")],
  bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᡇ"): bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᡈ"),
  bstack111l1l_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᡉ"): bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᡊ"),
  bstack111l1l_opy_ (u"ࠪࡥࡵࡶࠧᡋ"): bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࠧᡌ"),
  bstack111l1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᡍ"): bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᡎ"),
  bstack111l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡏ"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡐ"),
  bstack111l1l_opy_ (u"ࠤࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠢᡑ"): bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࠣᡒ"),
}
bstack11lllll11l_opy_ = {
  bstack111l1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᡓ"): bstack111l1l_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡔ"),
  bstack111l1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᡕ"): [bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡖ"), bstack111l1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᡗ")],
  bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᡘ"): bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᡙ"),
  bstack111l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᡚ"): bstack111l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᡛ"),
  bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᡜ"): [bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᡝ"), bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᡞ")],
  bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᡟ"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᡠ"),
  bstack111l1l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᡡ"): bstack111l1l_opy_ (u"ࠬࡸࡥࡢ࡮ࡢࡱࡴࡨࡩ࡭ࡧࠪᡢ"),
  bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᡣ"): [bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᡤ"), bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡥ")],
  bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨᡦ"): [bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࡶࠫᡧ"), bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࠫᡨ")]
}
bstack11l111l111_opy_ = [
  bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᡩ"),
  bstack111l1l_opy_ (u"࠭ࡰࡢࡩࡨࡐࡴࡧࡤࡔࡶࡵࡥࡹ࡫ࡧࡺࠩᡪ"),
  bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ᡫ"),
  bstack111l1l_opy_ (u"ࠨࡵࡨࡸ࡜࡯࡮ࡥࡱࡺࡖࡪࡩࡴࠨᡬ"),
  bstack111l1l_opy_ (u"ࠩࡷ࡭ࡲ࡫࡯ࡶࡶࡶࠫᡭ"),
  bstack111l1l_opy_ (u"ࠪࡷࡹࡸࡩࡤࡶࡉ࡭ࡱ࡫ࡉ࡯ࡶࡨࡶࡦࡩࡴࡢࡤ࡬ࡰ࡮ࡺࡹࠨᡮ"),
  bstack111l1l_opy_ (u"ࠫࡺࡴࡨࡢࡰࡧࡰࡪࡪࡐࡳࡱࡰࡴࡹࡈࡥࡩࡣࡹ࡭ࡴࡸࠧᡯ"),
  bstack111l1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᡰ"),
  bstack111l1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᡱ"),
  bstack111l1l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᡲ"),
  bstack111l1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᡳ"),
  bstack111l1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪᡴ"),
]
bstack1111llllll_opy_ = [
  bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᡵ"),
  bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨᡶ"),
  bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫᡷ"),
  bstack111l1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᡸ"),
  bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᡹"),
  bstack111l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ᡺"),
  bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᡻"),
  bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᡼"),
  bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ᡽"),
  bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ᡾"),
  bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᡿"),
  bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧᢀ"),
  bstack111l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪᢁ"),
  bstack111l1l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡖࡤ࡫ࠬᢂ"),
  bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᢃ"),
  bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᢄ"),
  bstack111l1l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᢅ"),
  bstack111l1l_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠵ࠬᢆ"),
  bstack111l1l_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠷࠭ᢇ"),
  bstack111l1l_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠹ࠧᢈ"),
  bstack111l1l_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠴ࠨᢉ"),
  bstack111l1l_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠶ࠩᢊ"),
  bstack111l1l_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠸ࠪᢋ"),
  bstack111l1l_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠺ࠫᢌ"),
  bstack111l1l_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠼ࠬᢍ"),
  bstack111l1l_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠾࠭ᢎ"),
  bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᢏ"),
  bstack111l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᢐ"),
  bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᢑ"),
  bstack111l1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ᢒ"),
  bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᢓ"),
  bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᢔ"),
  bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᢕ")
]
bstack11l1l11111l_opy_ = [
  bstack111l1l_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭ᢖ"),
  bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᢗ"),
  bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᢘ"),
  bstack111l1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᢙ"),
  bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡓࡶ࡮ࡵࡲࡪࡶࡼࠫᢚ"),
  bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᢛ"),
  bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚ࡡࡨࠩᢜ"),
  bstack111l1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᢝ"),
  bstack111l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᢞ"),
  bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᢟ"),
  bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᢠ"),
  bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫᢡ"),
  bstack111l1l_opy_ (u"࠭࡯ࡴࠩᢢ"),
  bstack111l1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᢣ"),
  bstack111l1l_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧᢤ"),
  bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫᢥ"),
  bstack111l1l_opy_ (u"ࠪࡶࡪ࡭ࡩࡰࡰࠪᢦ"),
  bstack111l1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭ᢧ"),
  bstack111l1l_opy_ (u"ࠬࡳࡡࡤࡪ࡬ࡲࡪ࠭ᢨ"),
  bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡲࡰࡺࡺࡩࡰࡰᢩࠪ"),
  bstack111l1l_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬᢪ"),
  bstack111l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬ᢫"),
  bstack111l1l_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨ᢬"),
  bstack111l1l_opy_ (u"ࠪࡲࡴࡖࡡࡨࡧࡏࡳࡦࡪࡔࡪ࡯ࡨࡳࡺࡺࠧ᢭"),
  bstack111l1l_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬ᢮"),
  bstack111l1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫ᢯"),
  bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᢰ"),
  bstack111l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡦࡰࡧࡏࡪࡿࡳࠨᢱ"),
  bstack111l1l_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬᢲ"),
  bstack111l1l_opy_ (u"ࠩࡱࡳࡕ࡯ࡰࡦ࡮࡬ࡲࡪ࠭ᢳ"),
  bstack111l1l_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡗࡕࡐࠬᢴ"),
  bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᢵ"),
  bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡈࡵ࡯࡬࡫ࡨࡷࠬᢶ"),
  bstack111l1l_opy_ (u"࠭ࡣࡢࡲࡷࡹࡷ࡫ࡃࡳࡣࡶ࡬ࠬᢷ"),
  bstack111l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᢸ"),
  bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᢹ"),
  bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᢺ"),
  bstack111l1l_opy_ (u"ࠪࡲࡴࡈ࡬ࡢࡰ࡮ࡔࡴࡲ࡬ࡪࡰࡪࠫᢻ"),
  bstack111l1l_opy_ (u"ࠫࡲࡧࡳ࡬ࡕࡨࡲࡩࡑࡥࡺࡵࠪᢼ"),
  bstack111l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡑࡵࡧࡴࠩᢽ"),
  bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡏࡤࠨᢾ"),
  bstack111l1l_opy_ (u"ࠧࡥࡧࡧ࡭ࡨࡧࡴࡦࡦࡇࡩࡻ࡯ࡣࡦࠩᢿ"),
  bstack111l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡑࡣࡵࡥࡲࡹࠧᣀ"),
  bstack111l1l_opy_ (u"ࠩࡳ࡬ࡴࡴࡥࡏࡷࡰࡦࡪࡸࠧᣁ"),
  bstack111l1l_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨᣂ"),
  bstack111l1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡑࡳࡸ࡮ࡵ࡮ࡴࠩᣃ"),
  bstack111l1l_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪᣄ"),
  bstack111l1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᣅ"),
  bstack111l1l_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᣆ"),
  bstack111l1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡃ࡫ࡲࡱࡪࡺࡲࡪࡥࠪᣇ"),
  bstack111l1l_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࡗ࠴ࠪᣈ"),
  bstack111l1l_opy_ (u"ࠪࡱ࡮ࡪࡓࡦࡵࡶ࡭ࡴࡴࡉ࡯ࡵࡷࡥࡱࡲࡁࡱࡲࡶࠫᣉ"),
  bstack111l1l_opy_ (u"ࠫࡪࡹࡰࡳࡧࡶࡷࡴ࡙ࡥࡳࡸࡨࡶࠬᣊ"),
  bstack111l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫᣋ"),
  bstack111l1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡄࡦࡳࠫᣌ"),
  bstack111l1l_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࠧᣍ"),
  bstack111l1l_opy_ (u"ࠨࡵࡼࡲࡨ࡚ࡩ࡮ࡧ࡚࡭ࡹ࡮ࡎࡕࡒࠪᣎ"),
  bstack111l1l_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧᣏ"),
  bstack111l1l_opy_ (u"ࠪ࡫ࡵࡹࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨᣐ"),
  bstack111l1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬᣑ"),
  bstack111l1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬᣒ"),
  bstack111l1l_opy_ (u"࠭ࡦࡰࡴࡦࡩࡈ࡮ࡡ࡯ࡩࡨࡎࡦࡸࠧᣓ"),
  bstack111l1l_opy_ (u"ࠧࡹ࡯ࡶࡎࡦࡸࠧᣔ"),
  bstack111l1l_opy_ (u"ࠨࡺࡰࡼࡏࡧࡲࠨᣕ"),
  bstack111l1l_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨᣖ"),
  bstack111l1l_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪᣗ"),
  bstack111l1l_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸࠬᣘ"),
  bstack111l1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨᣙ"),
  bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡙ࡩࡷࡹࡩࡰࡰࠪᣚ"),
  bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ᣛ"),
  bstack111l1l_opy_ (u"ࠨࡴࡨࡷ࡮࡭࡮ࡂࡲࡳࠫᣜ"),
  bstack111l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࡸ࠭ᣝ"),
  bstack111l1l_opy_ (u"ࠪࡧࡦࡴࡡࡳࡻࠪᣞ"),
  bstack111l1l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬᣟ"),
  bstack111l1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᣠ"),
  bstack111l1l_opy_ (u"࠭ࡩࡦࠩᣡ"),
  bstack111l1l_opy_ (u"ࠧࡦࡦࡪࡩࠬᣢ"),
  bstack111l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᣣ"),
  bstack111l1l_opy_ (u"ࠩࡴࡹࡪࡻࡥࠨᣤ"),
  bstack111l1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡰࡤࡰࠬᣥ"),
  bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡔࡶࡲࡶࡪࡉ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠬᣦ"),
  bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡈࡧ࡭ࡦࡴࡤࡍࡲࡧࡧࡦࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫᣧ"),
  bstack111l1l_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡉࡽࡩ࡬ࡶࡦࡨࡌࡴࡹࡴࡴࠩᣨ"),
  bstack111l1l_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡎࡴࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪᣩ"),
  bstack111l1l_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࠬᣪ"),
  bstack111l1l_opy_ (u"ࠩࡵࡩࡸ࡫ࡲࡷࡧࡇࡩࡻ࡯ࡣࡦࠩᣫ"),
  bstack111l1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᣬ"),
  bstack111l1l_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ᣭ"),
  bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕࡧࡳࡴࡥࡲࡨࡪ࠭ᣮ"),
  bstack111l1l_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡏ࡯ࡴࡆࡨࡺ࡮ࡩࡥࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᣯ"),
  bstack111l1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡶࡦ࡬ࡳࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧᣰ"),
  bstack111l1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡲࡳࡰࡪࡖࡡࡺࠩᣱ"),
  bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᣲ"),
  bstack111l1l_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨᣳ"),
  bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᣴ"),
  bstack111l1l_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩᣵ"),
  bstack111l1l_opy_ (u"࠭ࡨࡪࡩ࡫ࡇࡴࡴࡴࡳࡣࡶࡸࠬ᣶"),
  bstack111l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࠫ᣷"),
  bstack111l1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫ᣸"),
  bstack111l1l_opy_ (u"ࠩࡶ࡭ࡲࡕࡰࡵ࡫ࡲࡲࡸ࠭᣹"),
  bstack111l1l_opy_ (u"ࠪࡶࡪࡳ࡯ࡷࡧࡌࡓࡘࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࡏࡳࡨࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᣺"),
  bstack111l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭᣻"),
  bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᣼"),
  bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨ᣽"),
  bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭᣾"),
  bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ᣿"),
  bstack111l1l_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬᤀ"),
  bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩᤁ"),
  bstack111l1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭ᤂ"),
  bstack111l1l_opy_ (u"ࠬࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡑࡴࡲࡱࡵࡺࡂࡦࡪࡤࡺ࡮ࡵࡲࠨᤃ")
]
bstack111l1l1ll1_opy_ = {
  bstack111l1l_opy_ (u"࠭ࡶࠨᤄ"): bstack111l1l_opy_ (u"ࠧࡷࠩᤅ"),
  bstack111l1l_opy_ (u"ࠨࡨࠪᤆ"): bstack111l1l_opy_ (u"ࠩࡩࠫᤇ"),
  bstack111l1l_opy_ (u"ࠪࡪࡴࡸࡣࡦࠩᤈ"): bstack111l1l_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪᤉ"),
  bstack111l1l_opy_ (u"ࠬࡵ࡮࡭ࡻࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᤊ"): bstack111l1l_opy_ (u"࠭࡯࡯࡮ࡼࡅࡺࡺ࡯࡮ࡣࡷࡩࠬᤋ"),
  bstack111l1l_opy_ (u"ࠧࡧࡱࡵࡧࡪࡲ࡯ࡤࡣ࡯ࠫᤌ"): bstack111l1l_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬᤍ"),
  bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬᤎ"): bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ᤏ"),
  bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧᤐ"): bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨᤑ"),
  bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩᤒ"): bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᤓ"),
  bstack111l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫᤔ"): bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᤕ"),
  bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡨࡰࡵࡷࠫᤖ"): bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡉࡱࡶࡸࠬᤗ"),
  bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡲࡶࡹ࠭ᤘ"): bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧᤙ"),
  bstack111l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨᤚ"): bstack111l1l_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᤛ"),
  bstack111l1l_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫᤜ"): bstack111l1l_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬᤝ"),
  bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬᤞ"): bstack111l1l_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᤟"),
  bstack111l1l_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨᤠ"): bstack111l1l_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩᤡ"),
  bstack111l1l_opy_ (u"ࠨࡤ࡬ࡲࡦࡸࡹࡱࡣࡷ࡬ࠬᤢ"): bstack111l1l_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ᤣ"),
  bstack111l1l_opy_ (u"ࠪࡴࡦࡩࡦࡪ࡮ࡨࠫᤤ"): bstack111l1l_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᤥ"),
  bstack111l1l_opy_ (u"ࠬࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᤦ"): bstack111l1l_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩᤧ"),
  bstack111l1l_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪᤨ"): bstack111l1l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᤩ"),
  bstack111l1l_opy_ (u"ࠩ࡯ࡳ࡬࡬ࡩ࡭ࡧࠪᤪ"): bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫᤫ"),
  bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᤬"): bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᤭"),
  bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠨ᤮"): bstack111l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡲࡨࡥࡹ࡫ࡲࠨ᤯")
}
bstack11l1l111l1l_opy_ = bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪ࡭ࡹ࡮ࡵࡣ࠰ࡦࡳࡲ࠵ࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪ࠱ࡵࡩࡱ࡫ࡡࡴࡧࡶ࠳ࡱࡧࡴࡦࡵࡷ࠳ࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᤰ")
bstack11l1l111lll_opy_ = bstack111l1l_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠱࡫ࡩࡦࡲࡴࡩࡥ࡫ࡩࡨࡱࠢᤱ")
bstack1l1l1l111_opy_ = bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡪࡪࡳ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡸ࡫࡮ࡥࡡࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨᤲ")
bstack1l1ll1l1ll_opy_ = bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡽࡤ࠰ࡪࡸࡦࠬᤳ")
bstack11111lllll_opy_ = bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠨᤴ")
bstack1l1l11l1ll_opy_ = bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯࡯ࡧࡻࡸࡤ࡮ࡵࡣࡵࠪᤵ")
bstack11l11ll1l1l_opy_ = {
  bstack111l1l_opy_ (u"ࠧࡤࡴ࡬ࡸ࡮ࡩࡡ࡭ࠩᤶ"): 50,
  bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᤷ"): 40,
  bstack111l1l_opy_ (u"ࠩࡺࡥࡷࡴࡩ࡯ࡩࠪᤸ"): 30,
  bstack111l1l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ᤹"): 20,
  bstack111l1l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪ᤺"): 10
}
bstack111l111ll1_opy_ = bstack11l11ll1l1l_opy_[bstack111l1l_opy_ (u"ࠬ࡯࡮ࡧࡱ᤻ࠪ")]
bstack1l11l111ll_opy_ = bstack111l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬ᤼")
bstack1ll1llll1l_opy_ = bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬ᤽")
bstack11l11ll1ll_opy_ = bstack111l1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧ᤾")
bstack1lll1l1ll1_opy_ = bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨ᤿")
bstack1lll1ll1l_opy_ = bstack111l1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷࠤࡦࡴࡤࠡࡲࡼࡸࡪࡹࡴ࠮ࡵࡨࡰࡪࡴࡩࡶ࡯ࠣࡴࡦࡩ࡫ࡢࡩࡨࡷ࠳ࠦࡠࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸࠥࡶࡹࡵࡧࡶࡸ࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡠࠨ᥀")
bstack11l1l11ll11_opy_ = [bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬ᥁"), bstack111l1l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬ᥂")]
bstack11l11llllll_opy_ = [bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ᥃"), bstack111l1l_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ᥄")]
bstack111l11l111_opy_ = re.compile(bstack111l1l_opy_ (u"ࠨࡠ࡞ࡠࡡࡽ࠭࡞࠭࠽࠲࠯ࠪࠧ᥅"))
bstack11lll1l11_opy_ = [
  bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᥆"),
  bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᥇"),
  bstack111l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ᥈"),
  bstack111l1l_opy_ (u"ࠬࡴࡥࡸࡅࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࠩ᥉"),
  bstack111l1l_opy_ (u"࠭ࡡࡱࡲࠪ᥊"),
  bstack111l1l_opy_ (u"ࠧࡶࡦ࡬ࡨࠬ᥋"),
  bstack111l1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ᥌"),
  bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࠩ᥍"),
  bstack111l1l_opy_ (u"ࠪࡳࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨ᥎"),
  bstack111l1l_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࠩ᥏"),
  bstack111l1l_opy_ (u"ࠬࡴ࡯ࡓࡧࡶࡩࡹ࠭ᥐ"), bstack111l1l_opy_ (u"࠭ࡦࡶ࡮࡯ࡖࡪࡹࡥࡵࠩᥑ"),
  bstack111l1l_opy_ (u"ࠧࡤ࡮ࡨࡥࡷ࡙ࡹࡴࡶࡨࡱࡋ࡯࡬ࡦࡵࠪᥒ"),
  bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺࡔࡪ࡯࡬ࡲ࡬ࡹࠧᥓ"),
  bstack111l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࡒ࡯ࡨࡩ࡬ࡲ࡬࠭ᥔ"),
  bstack111l1l_opy_ (u"ࠪࡳࡹ࡮ࡥࡳࡃࡳࡴࡸ࠭ᥕ"),
  bstack111l1l_opy_ (u"ࠫࡵࡸࡩ࡯ࡶࡓࡥ࡬࡫ࡓࡰࡷࡵࡧࡪࡕ࡮ࡇ࡫ࡱࡨࡋࡧࡩ࡭ࡷࡵࡩࠬᥖ"),
  bstack111l1l_opy_ (u"ࠬࡧࡰࡱࡃࡦࡸ࡮ࡼࡩࡵࡻࠪᥗ"), bstack111l1l_opy_ (u"࠭ࡡࡱࡲࡓࡥࡨࡱࡡࡨࡧࠪᥘ"), bstack111l1l_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩᥙ"), bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡒࡤࡧࡰࡧࡧࡦࠩᥚ"), bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡇࡹࡷࡧࡴࡪࡱࡱࠫᥛ"),
  bstack111l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨᥜ"),
  bstack111l1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡩࡸࡺࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨᥝ"),
  bstack111l1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࠧᥞ"), bstack111l1l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࡆࡰࡧࡍࡳࡺࡥ࡯ࡶࠪᥟ"),
  bstack111l1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬᥠ"),
  bstack111l1l_opy_ (u"ࠨࡣࡧࡦࡕࡵࡲࡵࠩᥡ"),
  bstack111l1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡕࡲࡧࡰ࡫ࡴࠨᥢ"),
  bstack111l1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡘ࡮ࡳࡥࡰࡷࡷࠫᥣ"),
  bstack111l1l_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡴࡩࠩᥤ"),
  bstack111l1l_opy_ (u"ࠬࡧࡶࡥࠩᥥ"), bstack111l1l_opy_ (u"࠭ࡡࡷࡦࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩᥦ"), bstack111l1l_opy_ (u"ࠧࡢࡸࡧࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩᥧ"), bstack111l1l_opy_ (u"ࠨࡣࡹࡨࡆࡸࡧࡴࠩᥨ"),
  bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡑࡥࡺࡵࡷࡳࡷ࡫ࠧᥩ"), bstack111l1l_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡴࡩࠩᥪ"), bstack111l1l_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡴࡵࡺࡳࡷࡪࠧᥫ"),
  bstack111l1l_opy_ (u"ࠬࡱࡥࡺࡃ࡯࡭ࡦࡹࠧᥬ"), bstack111l1l_opy_ (u"࠭࡫ࡦࡻࡓࡥࡸࡹࡷࡰࡴࡧࠫᥭ"),
  bstack111l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩ᥮"), bstack111l1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡁࡳࡩࡶࠫ᥯"), bstack111l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࡈ࡮ࡸࠧᥰ"), bstack111l1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡅ࡫ࡶࡴࡳࡥࡎࡣࡳࡴ࡮ࡴࡧࡇ࡫࡯ࡩࠬᥱ"), bstack111l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡘࡷࡪ࡙ࡹࡴࡶࡨࡱࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨᥲ"),
  bstack111l1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࠨᥳ"), bstack111l1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࡵࠪᥴ"),
  bstack111l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡊࡩࡴࡣࡥࡰࡪࡈࡵࡪ࡮ࡧࡇ࡭࡫ࡣ࡬ࠩ᥵"),
  bstack111l1l_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࡚ࡩ࡮ࡧࡲࡹࡹ࠭᥶"),
  bstack111l1l_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡃࡦࡸ࡮ࡵ࡮ࠨ᥷"), bstack111l1l_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡆࡥࡹ࡫ࡧࡰࡴࡼࠫ᥸"), bstack111l1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡊࡱࡧࡧࡴࠩ᥹"), bstack111l1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡦࡲࡉ࡯ࡶࡨࡲࡹࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨ᥺"),
  bstack111l1l_opy_ (u"࠭ࡤࡰࡰࡷࡗࡹࡵࡰࡂࡲࡳࡓࡳࡘࡥࡴࡧࡷࠫ᥻"),
  bstack111l1l_opy_ (u"ࠧࡶࡰ࡬ࡧࡴࡪࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩ᥼"), bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡪࡺࡋࡦࡻࡥࡳࡦࡸࡤࠨ᥽"),
  bstack111l1l_opy_ (u"ࠩࡱࡳࡘ࡯ࡧ࡯ࠩ᥾"),
  bstack111l1l_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡘࡲ࡮ࡳࡰࡰࡴࡷࡥࡳࡺࡖࡪࡧࡺࡷࠬ᥿"),
  bstack111l1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡤࡳࡱ࡬ࡨ࡜ࡧࡴࡤࡪࡨࡶࡸ࠭ᦀ"),
  bstack111l1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᦁ"),
  bstack111l1l_opy_ (u"࠭ࡲࡦࡥࡵࡩࡦࡺࡥࡄࡪࡵࡳࡲ࡫ࡄࡳ࡫ࡹࡩࡷ࡙ࡥࡴࡵ࡬ࡳࡳࡹࠧᦂ"),
  bstack111l1l_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ᦃ"),
  bstack111l1l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡕࡧࡴࡩࠩᦄ"),
  bstack111l1l_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡖࡴࡪ࡫ࡤࠨᦅ"),
  bstack111l1l_opy_ (u"ࠪ࡫ࡵࡹࡅ࡯ࡣࡥࡰࡪࡪࠧᦆ"),
  bstack111l1l_opy_ (u"ࠫ࡮ࡹࡈࡦࡣࡧࡰࡪࡹࡳࠨᦇ"),
  bstack111l1l_opy_ (u"ࠬࡧࡤࡣࡇࡻࡩࡨ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᦈ"),
  bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࡙ࡣࡳ࡫ࡳࡸࠬᦉ"),
  bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡉ࡫ࡶࡪࡥࡨࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫᦊ"),
  bstack111l1l_opy_ (u"ࠨࡣࡸࡸࡴࡍࡲࡢࡰࡷࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠨᦋ"),
  bstack111l1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡑࡥࡹࡻࡲࡢ࡮ࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧᦌ"),
  bstack111l1l_opy_ (u"ࠪࡷࡾࡹࡴࡦ࡯ࡓࡳࡷࡺࠧᦍ"),
  bstack111l1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡩࡨࡈࡰࡵࡷࠫᦎ"),
  bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡘࡲࡱࡵࡣ࡬ࠩᦏ"), bstack111l1l_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰ࡚ࡹࡱࡧࠪᦐ"), bstack111l1l_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡋࡦࡻࠪᦑ"),
  bstack111l1l_opy_ (u"ࠨࡣࡸࡸࡴࡒࡡࡶࡰࡦ࡬ࠬᦒ"),
  bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡦࡥࡹࡉࡡࡱࡶࡸࡶࡪ࠭ᦓ"),
  bstack111l1l_opy_ (u"ࠪࡹࡳ࡯࡮ࡴࡶࡤࡰࡱࡕࡴࡩࡧࡵࡔࡦࡩ࡫ࡢࡩࡨࡷࠬᦔ"),
  bstack111l1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩ࡜࡯࡮ࡥࡱࡺࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳ࠭ᦕ"),
  bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡴࡵ࡬ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩᦖ"),
  bstack111l1l_opy_ (u"࠭ࡥ࡯ࡨࡲࡶࡨ࡫ࡁࡱࡲࡌࡲࡸࡺࡡ࡭࡮ࠪᦗ"),
  bstack111l1l_opy_ (u"ࠧࡦࡰࡶࡹࡷ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡳࡉࡣࡹࡩࡕࡧࡧࡦࡵࠪᦘ"), bstack111l1l_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡆࡨࡺࡹࡵ࡯࡭ࡵࡓࡳࡷࡺࠧᦙ"), bstack111l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡆࡨࡸࡦ࡯࡬ࡴࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠬᦚ"),
  bstack111l1l_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡴࡵࡹࡃࡢࡥ࡫ࡩࡑ࡯࡭ࡪࡶࠪᦛ"),
  bstack111l1l_opy_ (u"ࠫࡨࡧ࡬ࡦࡰࡧࡥࡷࡌ࡯ࡳ࡯ࡤࡸࠬᦜ"),
  bstack111l1l_opy_ (u"ࠬࡨࡵ࡯ࡦ࡯ࡩࡎࡪࠧᦝ"),
  bstack111l1l_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᦞ"),
  bstack111l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡈࡲࡦࡨ࡬ࡦࡦࠪᦟ"), bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡅࡺࡺࡨࡰࡴ࡬ࡾࡪࡪࠧᦠ"),
  bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵࡁࡤࡥࡨࡴࡹࡇ࡬ࡦࡴࡷࡷࠬᦡ"), bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯ࡅ࡫ࡶࡱ࡮ࡹࡳࡂ࡮ࡨࡶࡹࡹࠧᦢ"),
  bstack111l1l_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡳࡍ࡫ࡥࠫᦣ"),
  bstack111l1l_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡕࡣࡳࠫᦤ"),
  bstack111l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏ࡮ࡪࡶ࡬ࡥࡱ࡛ࡲ࡭ࠩᦥ"), bstack111l1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡁ࡭࡮ࡲࡻࡕࡵࡰࡶࡲࡶࠫᦦ"), bstack111l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡩࡱࡳࡷ࡫ࡆࡳࡣࡸࡨ࡜ࡧࡲ࡯࡫ࡱ࡫ࠬᦧ"), bstack111l1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡩࡳࡒࡩ࡯࡭ࡶࡍࡳࡈࡡࡤ࡭ࡪࡶࡴࡻ࡮ࡥࠩᦨ"),
  bstack111l1l_opy_ (u"ࠪ࡯ࡪ࡫ࡰࡌࡧࡼࡇ࡭ࡧࡩ࡯ࡵࠪᦩ"),
  bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡾࡦࡨ࡬ࡦࡕࡷࡶ࡮ࡴࡧࡴࡆ࡬ࡶࠬᦪ"),
  bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡥࡨࡷࡸࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨᦫ"),
  bstack111l1l_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡐ࡫ࡹࡅࡧ࡯ࡥࡾ࠭᦬"),
  bstack111l1l_opy_ (u"ࠧࡴࡪࡲࡻࡎࡕࡓࡍࡱࡪࠫ᦭"),
  bstack111l1l_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡕࡷࡶࡦࡺࡥࡨࡻࠪ᦮"),
  bstack111l1l_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡔࡨࡷࡵࡵ࡮ࡴࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᦯"), bstack111l1l_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡗࡢ࡫ࡷࡘ࡮ࡳࡥࡰࡷࡷࠫᦰ"),
  bstack111l1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࠧᦱ"),
  bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡹࡹ࡯ࡥࡈࡼࡪࡩࡵࡵࡧࡉࡶࡴࡳࡈࡵࡶࡳࡷࠬᦲ"),
  bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡃࡢࡲࡷࡹࡷ࡫ࠧᦳ"),
  bstack111l1l_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧᦴ"),
  bstack111l1l_opy_ (u"ࠨࡨࡸࡰࡱࡉ࡯࡯ࡶࡨࡼࡹࡒࡩࡴࡶࠪᦵ"),
  bstack111l1l_opy_ (u"ࠩࡺࡥ࡮ࡺࡆࡰࡴࡄࡴࡵ࡙ࡣࡳ࡫ࡳࡸࠬᦶ"),
  bstack111l1l_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡇࡴࡴ࡮ࡦࡥࡷࡖࡪࡺࡲࡪࡧࡶࠫᦷ"),
  bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡏࡣࡰࡩࠬᦸ"),
  bstack111l1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡙ࡌࡄࡧࡵࡸࠬᦹ"),
  bstack111l1l_opy_ (u"࠭ࡴࡢࡲ࡚࡭ࡹ࡮ࡓࡩࡱࡵࡸࡕࡸࡥࡴࡵࡇࡹࡷࡧࡴࡪࡱࡱࠫᦺ"),
  bstack111l1l_opy_ (u"ࠧࡴࡥࡤࡰࡪࡌࡡࡤࡶࡲࡶࠬᦻ"),
  bstack111l1l_opy_ (u"ࠨࡹࡧࡥࡑࡵࡣࡢ࡮ࡓࡳࡷࡺࠧᦼ"),
  bstack111l1l_opy_ (u"ࠩࡶ࡬ࡴࡽࡘࡤࡱࡧࡩࡑࡵࡧࠨᦽ"),
  bstack111l1l_opy_ (u"ࠪ࡭ࡴࡹࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡷࡶࡩࠬᦾ"),
  bstack111l1l_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪ࠭ᦿ"),
  bstack111l1l_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡵࡶࡻࡴࡸࡤࠨᧀ"),
  bstack111l1l_opy_ (u"࠭ࡵࡴࡧࡓࡶࡪࡨࡵࡪ࡮ࡷ࡛ࡉࡇࠧᧁ"),
  bstack111l1l_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡘࡆࡄࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠨᧂ"),
  bstack111l1l_opy_ (u"ࠨࡹࡨࡦࡉࡸࡩࡷࡧࡵࡅ࡬࡫࡮ࡵࡗࡵࡰࠬᧃ"),
  bstack111l1l_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡺࡨࠨᧄ"),
  bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡎࡦࡹ࡚ࡈࡆ࠭ᧅ"),
  bstack111l1l_opy_ (u"ࠫࡼࡪࡡࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧᧆ"), bstack111l1l_opy_ (u"ࠬࡽࡤࡢࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࡙࡯࡭ࡦࡱࡸࡸࠬᧇ"),
  bstack111l1l_opy_ (u"࠭ࡸࡤࡱࡧࡩࡔࡸࡧࡊࡦࠪᧈ"), bstack111l1l_opy_ (u"ࠧࡹࡥࡲࡨࡪ࡙ࡩࡨࡰ࡬ࡲ࡬ࡏࡤࠨᧉ"),
  bstack111l1l_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥ࡙ࡇࡅࡇࡻ࡮ࡥ࡮ࡨࡍࡩ࠭᧊"),
  bstack111l1l_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡐࡰࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡸࡴࡐࡰ࡯ࡽࠬ᧋"),
  bstack111l1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࡷࠬ᧌"),
  bstack111l1l_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶ࡮࡫ࡳࠨ᧍"), bstack111l1l_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷࡿࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠨ᧎"),
  bstack111l1l_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࡈࡢࡴࡧࡻࡦࡸࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩ᧏"),
  bstack111l1l_opy_ (u"ࠧ࡮ࡣࡻࡘࡾࡶࡩ࡯ࡩࡉࡶࡪࡷࡵࡦࡰࡦࡽࠬ᧐"),
  bstack111l1l_opy_ (u"ࠨࡵ࡬ࡱࡵࡲࡥࡊࡵ࡙࡭ࡸ࡯ࡢ࡭ࡧࡆ࡬ࡪࡩ࡫ࠨ᧑"),
  bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡉࡡࡳࡶ࡫ࡥ࡬࡫ࡓࡴ࡮ࠪ᧒"),
  bstack111l1l_opy_ (u"ࠪࡷ࡭ࡵࡵ࡭ࡦࡘࡷࡪ࡙ࡩ࡯ࡩ࡯ࡩࡹࡵ࡮ࡕࡧࡶࡸࡒࡧ࡮ࡢࡩࡨࡶࠬ᧓"),
  bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡌ࡛ࡉࡖࠧ᧔"),
  bstack111l1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡴࡻࡣࡩࡋࡧࡉࡳࡸ࡯࡭࡮ࠪ᧕"),
  bstack111l1l_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪࡎࡩࡥࡦࡨࡲࡆࡶࡩࡑࡱ࡯࡭ࡨࡿࡅࡳࡴࡲࡶࠬ᧖"),
  bstack111l1l_opy_ (u"ࠧ࡮ࡱࡦ࡯ࡑࡵࡣࡢࡶ࡬ࡳࡳࡇࡰࡱࠩ᧗"),
  bstack111l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇࡱࡵࡱࡦࡺࠧ᧘"), bstack111l1l_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈ࡬ࡰࡹ࡫ࡲࡔࡲࡨࡧࡸ࠭᧙"),
  bstack111l1l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡆࡨࡰࡦࡿࡁࡥࡤࠪ᧚"),
  bstack111l1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡎࡪࡌࡰࡥࡤࡸࡴࡸࡁࡶࡶࡲࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠧ᧛")
]
bstack111lll1lll_opy_ = bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡺࡶ࡬ࡰࡣࡧࠫ᧜")
bstack111l1l1111_opy_ = [bstack111l1l_opy_ (u"࠭࠮ࡢࡲ࡮ࠫ᧝"), bstack111l1l_opy_ (u"ࠧ࠯ࡣࡤࡦࠬ᧞"), bstack111l1l_opy_ (u"ࠨ࠰࡬ࡴࡦ࠭᧟")]
bstack111ll1lll_opy_ = [bstack111l1l_opy_ (u"ࠩ࡬ࡨࠬ᧠"), bstack111l1l_opy_ (u"ࠪࡴࡦࡺࡨࠨ᧡"), bstack111l1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ᧢"), bstack111l1l_opy_ (u"ࠬࡹࡨࡢࡴࡨࡥࡧࡲࡥࡠ࡫ࡧࠫ᧣")]
bstack111l1l1l11_opy_ = {
  bstack111l1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᧤"): bstack111l1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧥"),
  bstack111l1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᧦"): bstack111l1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ᧧"),
  bstack111l1l_opy_ (u"ࠪࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᧨"): bstack111l1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧩"),
  bstack111l1l_opy_ (u"ࠬ࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᧪"): bstack111l1l_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧫"),
  bstack111l1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡏࡱࡶ࡬ࡳࡳࡹࠧ᧬"): bstack111l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᧭")
}
bstack11l11111l1_opy_ = [
  bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ᧮"),
  bstack111l1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨ᧯"),
  bstack111l1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧰"),
  bstack111l1l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᧱"),
  bstack111l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ᧲"),
]
bstack1lll111lll_opy_ = bstack1111llllll_opy_ + bstack11l1l11111l_opy_ + bstack11lll1l11_opy_
bstack1l1111llll_opy_ = [
  bstack111l1l_opy_ (u"ࠧ࡟࡮ࡲࡧࡦࡲࡨࡰࡵࡷࠨࠬ᧳"),
  bstack111l1l_opy_ (u"ࠨࡠࡥࡷ࠲ࡲ࡯ࡤࡣ࡯࠲ࡨࡵ࡭ࠥࠩ᧴"),
  bstack111l1l_opy_ (u"ࠩࡡ࠵࠷࠽࠮ࠨ᧵"),
  bstack111l1l_opy_ (u"ࠪࡢ࠶࠶࠮ࠨ᧶"),
  bstack111l1l_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠴࡟࠻࠳࠹࡞࠰ࠪ᧷"),
  bstack111l1l_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠶ࡠ࠶࠭࠺࡟࠱ࠫ᧸"),
  bstack111l1l_opy_ (u"࠭࡞࠲࠹࠵࠲࠸ࡡ࠰࠮࠳ࡠ࠲ࠬ᧹"),
  bstack111l1l_opy_ (u"ࠧ࡟࠳࠼࠶࠳࠷࠶࠹࠰ࠪ᧺")
]
bstack11l1l111ll1_opy_ = bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ᧻")
bstack11l1ll111_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰ࠵ࡶ࠲࠱ࡨࡺࡪࡴࡴࠨ᧼")
bstack11l1lll1l1_opy_ = [ bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ᧽") ]
bstack1ll1ll1ll1_opy_ = [ bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪ᧾") ]
bstack11ll1l11l1_opy_ = [bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ᧿")]
bstack1l1ll1ll11_opy_ = [ bstack111l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᨀ") ]
bstack11l1ll1ll_opy_ = bstack111l1l_opy_ (u"ࠧࡔࡆࡎࡗࡪࡺࡵࡱࠩᨁ")
bstack11llll1l1_opy_ = bstack111l1l_opy_ (u"ࠨࡕࡇࡏ࡙࡫ࡳࡵࡃࡷࡸࡪࡳࡰࡵࡧࡧࠫᨂ")
bstack1l1l11llll_opy_ = bstack111l1l_opy_ (u"ࠩࡖࡈࡐ࡚ࡥࡴࡶࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱ࠭ᨃ")
bstack1ll11ll1l1_opy_ = bstack111l1l_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࠩᨄ")
bstack11111ll11_opy_ = [
  bstack111l1l_opy_ (u"ࠫࡊࡘࡒࡠࡈࡄࡍࡑࡋࡄࠨᨅ"),
  bstack111l1l_opy_ (u"ࠬࡋࡒࡓࡡࡗࡍࡒࡋࡄࡠࡑࡘࡘࠬᨆ"),
  bstack111l1l_opy_ (u"࠭ࡅࡓࡔࡢࡆࡑࡕࡃࡌࡇࡇࡣࡇ࡟࡟ࡄࡎࡌࡉࡓ࡚ࠧᨇ"),
  bstack111l1l_opy_ (u"ࠧࡆࡔࡕࡣࡓࡋࡔࡘࡑࡕࡏࡤࡉࡈࡂࡐࡊࡉࡉ࠭ᨈ"),
  bstack111l1l_opy_ (u"ࠨࡇࡕࡖࡤ࡙ࡏࡄࡍࡈࡘࡤࡔࡏࡕࡡࡆࡓࡓࡔࡅࡄࡖࡈࡈࠬᨉ"),
  bstack111l1l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡇࡑࡕࡓࡆࡆࠪᨊ"),
  bstack111l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡗࡋࡓࡆࡖࠪᨋ"),
  bstack111l1l_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡘࡅࡇࡗࡖࡉࡉ࠭ᨌ"),
  bstack111l1l_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡁࡃࡑࡕࡘࡊࡊࠧᨍ"),
  bstack111l1l_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᨎ"),
  bstack111l1l_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡑࡓ࡙ࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࠨᨏ"),
  bstack111l1l_opy_ (u"ࠨࡇࡕࡖࡤࡇࡄࡅࡔࡈࡗࡘࡥࡉࡏࡘࡄࡐࡎࡊࠧᨐ"),
  bstack111l1l_opy_ (u"ࠩࡈࡖࡗࡥࡁࡅࡆࡕࡉࡘ࡙࡟ࡖࡐࡕࡉࡆࡉࡈࡂࡄࡏࡉࠬᨑ"),
  bstack111l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡕࡗࡑࡒࡊࡒ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᨒ"),
  bstack111l1l_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤ࡚ࡉࡎࡇࡇࡣࡔ࡛ࡔࠨᨓ"),
  bstack111l1l_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡓࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᨔ"),
  bstack111l1l_opy_ (u"࠭ࡅࡓࡔࡢࡗࡔࡉࡋࡔࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡈࡐࡕࡗࡣ࡚ࡔࡒࡆࡃࡆࡌࡆࡈࡌࡆࠩᨕ"),
  bstack111l1l_opy_ (u"ࠧࡆࡔࡕࡣࡕࡘࡏ࡙࡛ࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᨖ"),
  bstack111l1l_opy_ (u"ࠨࡇࡕࡖࡤࡔࡁࡎࡇࡢࡒࡔ࡚࡟ࡓࡇࡖࡓࡑ࡜ࡅࡅࠩᨗ"),
  bstack111l1l_opy_ (u"ࠩࡈࡖࡗࡥࡎࡂࡏࡈࡣࡗࡋࡓࡐࡎࡘࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨᨘ"),
  bstack111l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡎࡃࡑࡈࡆ࡚ࡏࡓ࡛ࡢࡔࡗࡕࡘ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩᨙ"),
]
bstack1ll11111l_opy_ = bstack111l1l_opy_ (u"ࠫ࠳࠵ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡧࡲࡵ࡫ࡩࡥࡨࡺࡳ࠰ࠩᨚ")
bstack111l11111_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠬࢄࠧᨛ")), bstack111l1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭᨜"), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᨝"))
bstack11l1l111111_opy_ = bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡰࡪࠩ᨞")
bstack11l11ll1111_opy_ = [ bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ᨟"), bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩᨠ"), bstack111l1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪᨡ"), bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬᨢ")]
bstack1l11l1llll_opy_ = [ bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᨣ"), bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ᨤ"), bstack111l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧᨥ"), bstack111l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩᨦ") ]
bstack1llll111ll_opy_ = [ bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩᨧ") ]
bstack11l11l1l1l1_opy_ = [ bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᨨ") ]
bstack11l1111l1l_opy_ = 360
bstack11ll11l1l1l_opy_ = bstack111l1l_opy_ (u"ࠧࡧࡰࡱ࠯ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧᨩ")
bstack11l11l1l111_opy_ = bstack111l1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰࡫ࡶࡷࡺ࡫ࡳࠣᨪ")
bstack11l1l1111ll_opy_ = bstack111l1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡤࡴ࡮࠵ࡶ࠲࠱࡬ࡷࡸࡻࡥࡴ࠯ࡶࡹࡲࡳࡡࡳࡻࠥᨫ")
bstack11l1l11l1l1_opy_ = bstack111l1l_opy_ (u"ࠣࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡷࡩࡸࡺࡳࠡࡣࡵࡩࠥࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡱࡱࠤࡔ࡙ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࠧࡶࠤࡦࡴࡤࠡࡣࡥࡳࡻ࡫ࠠࡧࡱࡵࠤࡆࡴࡤࡳࡱ࡬ࡨࠥࡪࡥࡷ࡫ࡦࡩࡸ࠴ࠢᨬ")
bstack11l1l11l1ll_opy_ = bstack111l1l_opy_ (u"ࠤ࠴࠵࠳࠶ࠢᨭ")
bstack1l111111_opy_ = {
  bstack111l1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨᨮ"): bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᨯ"),
  bstack111l1l_opy_ (u"ࠬࡌࡁࡊࡎࠪᨰ"): bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᨱ"),
  bstack111l1l_opy_ (u"ࠧࡔࡍࡌࡔࠬᨲ"): bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᨳ")
}
bstack11ll11111l_opy_ = [
  bstack111l1l_opy_ (u"ࠤࡪࡩࡹࠨᨴ"),
  bstack111l1l_opy_ (u"ࠥ࡫ࡴࡈࡡࡤ࡭ࠥᨵ"),
  bstack111l1l_opy_ (u"ࠦ࡬ࡵࡆࡰࡴࡺࡥࡷࡪࠢᨶ"),
  bstack111l1l_opy_ (u"ࠧࡸࡥࡧࡴࡨࡷ࡭ࠨᨷ"),
  bstack111l1l_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࡊࡲࡥ࡮ࡧࡱࡸࠧᨸ"),
  bstack111l1l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᨹ"),
  bstack111l1l_opy_ (u"ࠣࡵࡸࡦࡲ࡯ࡴࡆ࡮ࡨࡱࡪࡴࡴࠣᨺ"),
  bstack111l1l_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡋ࡬ࡦ࡯ࡨࡲࡹࠨᨻ"),
  bstack111l1l_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡁࡤࡶ࡬ࡺࡪࡋ࡬ࡦ࡯ࡨࡲࡹࠨᨼ"),
  bstack111l1l_opy_ (u"ࠦࡨࡲࡥࡢࡴࡈࡰࡪࡳࡥ࡯ࡶࠥᨽ"),
  bstack111l1l_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࡸࠨᨾ"),
  bstack111l1l_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹࠨᨿ"),
  bstack111l1l_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࡂࡵࡼࡲࡨ࡙ࡣࡳ࡫ࡳࡸࠧᩀ"),
  bstack111l1l_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢᩁ"),
  bstack111l1l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᩂ"),
  bstack111l1l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡘࡴࡻࡣࡩࡃࡦࡸ࡮ࡵ࡮ࠣᩃ"),
  bstack111l1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡒࡻ࡬ࡵ࡫ࡗࡳࡺࡩࡨࠣᩄ"),
  bstack111l1l_opy_ (u"ࠧࡹࡨࡢ࡭ࡨࠦᩅ"),
  bstack111l1l_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࡆࡶࡰࠣᩆ")
]
bstack11l11lll111_opy_ = [
  bstack111l1l_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࠨᩇ"),
  bstack111l1l_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᩈ"),
  bstack111l1l_opy_ (u"ࠤࡤࡹࡹࡵࠢᩉ"),
  bstack111l1l_opy_ (u"ࠥࡱࡦࡴࡵࡢ࡮ࠥᩊ"),
  bstack111l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᩋ")
]
bstack11l1lllll_opy_ = {
  bstack111l1l_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࠦᩌ"): [bstack111l1l_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࡊࡲࡥ࡮ࡧࡱࡸࠧᩍ")],
  bstack111l1l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᩎ"): [bstack111l1l_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᩏ")],
  bstack111l1l_opy_ (u"ࠤࡤࡹࡹࡵࠢᩐ"): [bstack111l1l_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡅ࡭ࡧࡰࡩࡳࡺࠢᩑ"), bstack111l1l_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸ࡚࡯ࡂࡥࡷ࡭ࡻ࡫ࡅ࡭ࡧࡰࡩࡳࡺࠢᩒ"), bstack111l1l_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᩓ"), bstack111l1l_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࡊࡲࡥ࡮ࡧࡱࡸࠧᩔ")],
  bstack111l1l_opy_ (u"ࠢ࡮ࡣࡱࡹࡦࡲࠢᩕ"): [bstack111l1l_opy_ (u"ࠣ࡯ࡤࡲࡺࡧ࡬ࠣᩖ")],
  bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᩗ"): [bstack111l1l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᩘ")],
}
bstack11l1l111l11_opy_ = {
  bstack111l1l_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥᩙ"): bstack111l1l_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࠦᩚ"),
  bstack111l1l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩛ"): bstack111l1l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᩜ"),
  bstack111l1l_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡊࡲࡥ࡮ࡧࡱࡸࠧᩝ"): bstack111l1l_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࠦᩞ"),
  bstack111l1l_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡁࡤࡶ࡬ࡺࡪࡋ࡬ࡦ࡯ࡨࡲࡹࠨ᩟"): bstack111l1l_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸࠨ᩠"),
  bstack111l1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᩡ"): bstack111l1l_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᩢ")
}
bstack1l11llll_opy_ = {
  bstack111l1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᩣ"): bstack111l1l_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࠠࡔࡧࡷࡹࡵ࠭ᩤ"),
  bstack111l1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬᩥ"): bstack111l1l_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࠢࡗࡩࡦࡸࡤࡰࡹࡱࠫᩦ"),
  bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᩧ"): bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࠣࡗࡪࡺࡵࡱࠩᩨ"),
  bstack111l1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᩩ"): bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸ࡚ࠥࡥࡢࡴࡧࡳࡼࡴࠧᩪ")
}
bstack11l1l11ll1l_opy_ = 65536
bstack11l11ll111l_opy_ = bstack111l1l_opy_ (u"ࠨ࠰࠱࠲ࡠ࡚ࡒࡖࡐࡆࡅ࡙ࡋࡄ࡞ࠩᩫ")
bstack11l1l1l11l1_opy_ = [
      bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᩬ"), bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᩭ"), bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᩮ"), bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᩯ"), bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᩰ"),
      bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᩱ"), bstack111l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫᩲ"), bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᩳ"), bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡢࡵࡶࠫᩴ"),
      bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ᩵"), bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ᩶"), bstack111l1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ᩷")
    ]
bstack11l11ll11ll_opy_= {
  bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᩸"): bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ᩹"),
  bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᩺"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ᩻"),
  bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ᩼"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᩽"),
  bstack111l1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭᩾"): bstack111l1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳ᩿ࠧ"),
  bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᪀"): bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᪁"),
  bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬ᪂"): bstack111l1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭᪃"),
  bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᪄"): bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᪅"),
  bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᪆"): bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᪇"),
  bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ᪈"): bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᪉"),
  bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪊"): bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ᪋"),
  bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᪌"): bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᪍"),
  bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨ᪎"): bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩ᪏"),
  bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᪐"): bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᪑"),
  bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬ᪒"): bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࡕࡰࡵ࡫ࡲࡲࡸ࠭᪓"),
  bstack111l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩ᪔"): bstack111l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪ᪕"),
  bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᪖"): bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᪗"),
  bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᪘"): bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ᪙"),
  bstack111l1l_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪ᪚"): bstack111l1l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫ᪛"),
  bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ᪜"): bstack111l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ᪝"),
  bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪞"): bstack111l1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᪟"),
  bstack111l1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨ᪠"): bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩ᪡"),
  bstack111l1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ᪢"): bstack111l1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪ᪣"),
  bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᪤"): bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᪥"),
  bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᪦"): bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᪧ"),
  bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ᪨"): bstack111l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ᪩"),
  bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ᪪"): bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᪫"),
  bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᪬"): bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᪭"),
  bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬ᪮"): bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭᪯")
}
bstack11l11lllll1_opy_ = [bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ᪰"), bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ᪱")]
bstack1ll111111_opy_ = (bstack111l1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤ᪲"),)
bstack11l11l1l11l_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠯ࡷ࠳࠲ࡹࡵࡪࡡࡵࡧࡢࡧࡱ࡯ࠧ᪳")
bstack1l11l1lll1_opy_ = bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠭ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠳ࡻ࠷࠯ࡨࡴ࡬ࡨࡸ࠵ࠢ᪴")
bstack1lll11ll1l_opy_ = bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡧࡳ࡫ࡧ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡥࡣࡶ࡬ࡧࡵࡡࡳࡦ࠲ࡦࡺ࡯࡬ࡥࡵ࠲᪵ࠦ")
bstack11llll1l11_opy_ = bstack111l1l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠯ࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴ᪶ࠢ")
class EVENTS(Enum):
  bstack11l11l1l1ll_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡴ࠷࠱ࡺ࠼ࡳࡶ࡮ࡴࡴ࠮ࡤࡸ࡭ࡱࡪ࡬ࡪࡰ࡮᪷ࠫ")
  bstack1111l1ll1l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡦࡣࡱࡹࡵ᪸࠭") # final bstack11l11l1ll11_opy_
  bstack11l1l1l111l_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡳࡦࡰࡧࡰࡴ࡭ࡳࠨ᪹")
  bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠾ࡵࡸࡩ࡯ࡶ࠰ࡦࡺ࡯࡬ࡥ࡮࡬ࡲࡰ᪺࠭") #shift post bstack11l11llll11_opy_
  bstack11ll1ll11_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡴࡷ࡯࡮ࡵ࠯ࡥࡹ࡮ࡲࡤ࡭࡫ࡱ࡯ࠬ᪻") #shift post bstack11l11llll11_opy_
  bstack11l11lll11l_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡩࡸࡺࡨࡶࡤࠪ᪼") #shift
  bstack11l1l11l111_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺ࠼ࡧࡳࡼࡴ࡬ࡰࡣࡧ᪽ࠫ") #shift
  bstack11l11ll11_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥ࠻ࡪࡸࡦ࠲ࡳࡡ࡯ࡣࡪࡩࡲ࡫࡮ࡵࠩ᪾")
  bstack1l111ll111l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧ࠱࠲ࡻ࠽ࡷࡦࡼࡥ࠮ࡴࡨࡷࡺࡲࡴࡴᪿࠩ")
  bstack1ll111l1l1_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡ࠲࠳ࡼ࠾ࡩࡸࡩࡷࡧࡵ࠱ࡵ࡫ࡲࡧࡱࡵࡱࡸࡩࡡ࡯ᫀࠩ")
  bstack11ll11l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼࡯ࡳࡨࡧ࡬ࠨ᫁") #shift
  bstack11l11ll11l_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡢࡲࡳ࠱ࡺࡶ࡬ࡰࡣࡧࠫ᫂") #shift
  bstack1l11lll1ll_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠾ࡨ࡯࠭ࡢࡴࡷ࡭࡫ࡧࡣࡵࡵ᫃ࠪ")
  bstack111llllll1_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࠶࠷ࡹ࠻ࡩࡨࡸ࠲ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠲ࡸࡥࡴࡷ࡯ࡸࡸ࠳ࡳࡶ࡯ࡰࡥࡷࡿ᫄ࠧ") #shift
  bstack1l1ll1l111_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࠷࠱ࡺ࠼ࡪࡩࡹ࠳ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠳ࡲࡦࡵࡸࡰࡹࡹࠧ᫅") #shift
  bstack11l1l11llll_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡥࡳࡥࡼࠫ᫆") #shift
  bstack11lllll111l_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡰࡦࡴࡦࡽ࠿ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ᫇")
  bstack11lll1ll1_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡶࡩࡸࡹࡩࡰࡰ࠰ࡷࡹࡧࡴࡶࡵࠪ᫈") #shift
  bstack1l1l1ll11l_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽࡬ࡺࡨ࠭࡮ࡣࡱࡥ࡬࡫࡭ࡦࡰࡷࠫ᫉")
  bstack11l11ll1l11_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡶࡴࡾࡹ࠮ࡵࡨࡸࡺࡶ᫊ࠧ") #shift
  bstack111l1ll1ll_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡷࡪࡺࡵࡱࠩ᫋")
  bstack11l11l1ll1l_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻ࠽ࡷࡳࡧࡰࡴࡪࡲࡸࠬᫌ") # not bstack11l11ll1lll_opy_ in python
  bstack1lll1lll1l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡷࡵࡪࡶࠪᫍ") # used in bstack11l11lll1l1_opy_
  bstack11l111ll11_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡧࡦࡶࠪᫎ") # used in bstack11l11lll1l1_opy_
  bstack1l111lllll_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡩࡱࡲ࡯ࠬ᫏")
  bstack1lll11l11l_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡷࡪࡹࡳࡪࡱࡱ࠱ࡳࡧ࡭ࡦࠩ᫐")
  bstack1l1lll111l_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠾ࡸ࡫ࡳࡴ࡫ࡲࡲ࠲ࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠩ᫑") #
  bstack11llll1111_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡳ࠶࠷ࡹ࠻ࡦࡵ࡭ࡻ࡫ࡲ࠮ࡶࡤ࡯ࡪ࡙ࡣࡳࡧࡨࡲࡘ࡮࡯ࡵࠩ᫒")
  bstack1111l1lll_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻ࠽ࡥࡺࡺ࡯࠮ࡥࡤࡴࡹࡻࡲࡦࠩ᫓")
  bstack11l1l1111l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡲࡦ࠯ࡷࡩࡸࡺࠧ᫔")
  bstack1l1l1lll1_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡰࡰࡵࡷ࠱ࡹ࡫ࡳࡵࠩ᫕")
  bstack1lll11111l_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡴࡨ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬ᫖") #shift
  bstack1lllll1ll1_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲ࠻ࡲࡲࡷࡹ࠳ࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡣࡷ࡭ࡴࡴࠧ᫗") #shift
  bstack11l1l11lll1_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡹࡹࡵ࠭ࡤࡣࡳࡸࡺࡸࡥࠨ᫘")
  bstack11l11lll1ll_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿࡯ࡤ࡭ࡧ࠰ࡸ࡮ࡳࡥࡰࡷࡷࠫ᫙")
  bstack1l1l1l1l11l_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡵࡷࡥࡷࡺࠧ᫚")
  bstack11l1l1l1111_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡧࡳࡼࡴ࡬ࡰࡣࡧࠫ᫛")
  bstack11l11ll11l1_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡧ࡭࡫ࡣ࡬࠯ࡸࡴࡩࡧࡴࡦࠩ᫜")
  bstack1l1l11ll111_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡴࡴ࠭ࡣࡱࡲࡸࡸࡺࡲࡢࡲࠪ᫝")
  bstack1l1l11lll1l_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡵ࡮࠮ࡥࡲࡲࡳ࡫ࡣࡵࠩ᫞")
  bstack1l11ll1l11l_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀ࡯࡯࠯ࡶࡸࡴࡶࠧ᫟")
  bstack1l11lll1lll_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡷࡹࡧࡲࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲࠬ᫠")
  bstack1l1l1l1l1l1_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡵ࡮࡯ࡧࡦࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࠨ᫡")
  bstack11l11ll1ll1_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶࡎࡴࡩࡵࠩ᫢")
  bstack11l11llll1l_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡦࡪࡰࡧࡒࡪࡧࡲࡦࡵࡷࡌࡺࡨࠧ᫣")
  bstack1llll1lllll_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰࡏ࡮ࡪࡶࠪ᫤")
  bstack1llll1l1ll1_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡵࡸࠬ᫥")
  bstack1l1111l11ll_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡅࡲࡲ࡫࡯ࡧࠨ᫦")
  bstack11l1l11l11l_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡆࡳࡳ࡬ࡩࡨࠩ᫧")
  bstack1l1ll111l11_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࡯ࡓࡦ࡮ࡩࡌࡪࡧ࡬ࡔࡶࡨࡴࠬ᫨")
  bstack1l1ll11l11l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡩࡔࡧ࡯ࡪࡍ࡫ࡡ࡭ࡉࡨࡸࡗ࡫ࡳࡶ࡮ࡷࠫ᫩")
  bstack1l111ll1lll_opy_ = bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡀࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰࡋࡶࡦࡰࡷࠫ᫪")
  bstack1l111llll1l_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡧࡶࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡊࡼࡥ࡯ࡶࠪ᫫")
  bstack1l111llll11_opy_ = bstack111l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡲ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࡇࡹࡩࡳࡺࠧ᫬")
  bstack11l1l1111l1_opy_ = bstack111l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡥ࡯ࡳࡸࡩࡺ࡫ࡔࡦࡵࡷࡉࡻ࡫࡮ࡵࠩ᫭")
  bstack1lllll111l1_opy_ = bstack111l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡳࡵ࠭᫮")
  bstack1l1l111l111_opy_ = bstack111l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡴࡴࡓࡵࡱࡳࠫ᫯")
class STAGE(Enum):
  bstack11ll1l111l_opy_ = bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࠧ᫰")
  END = bstack111l1l_opy_ (u"ࠩࡨࡲࡩ࠭᫱")
  bstack1ll1ll111_opy_ = bstack111l1l_opy_ (u"ࠪࡷ࡮ࡴࡧ࡭ࡧࠪ᫲")
bstack1l1l11111_opy_ = {
  bstack111l1l_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࠫ᫳"): bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᫴"),
  bstack111l1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪ᫵"): bstack111l1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩ᫶")
}
PLAYWRIGHT_HUB_URL = bstack111l1l_opy_ (u"ࠣࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠥ᫷")
bstack1l111l1111l_opy_ = 98
bstack1l111ll11l1_opy_ = 100
bstack111l1l1l_opy_ = {
  bstack111l1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࠨ᫸"): bstack111l1l_opy_ (u"ࠪ࠱࠲ࡸࡥࡳࡷࡱࡷࠬ᫹"),
  bstack111l1l_opy_ (u"ࠫࡩ࡫࡬ࡢࡻࠪ᫺"): bstack111l1l_opy_ (u"ࠬ࠳࠭ࡳࡧࡵࡹࡳࡹ࠭ࡥࡧ࡯ࡥࡾ࠭᫻"),
  bstack111l1l_opy_ (u"࠭ࡲࡦࡴࡸࡲ࠲ࡪࡥ࡭ࡣࡼࠫ᫼"): 0
}
bstack11ll1l1l11l_opy_ = bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢ᫽")
bstack11l11l1lll1_opy_ = bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡸࡴࡱࡵࡡࡥ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧ᫾")
bstack1111lll1l1_opy_ = bstack111l1l_opy_ (u"ࠤࡗࡉࡘ࡚ࠠࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠣࡅࡓࡊࠠࡂࡐࡄࡐ࡞࡚ࡉࡄࡕࠥ᫿")