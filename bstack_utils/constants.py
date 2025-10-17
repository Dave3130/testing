# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import re
from enum import Enum
bstack1l11111ll1_opy_ = {
  bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩធ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡶࠬន"),
  bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬប"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡮ࡩࡾ࠭ផ"),
  bstack11l111_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧព"): bstack11l111_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩភ"),
  bstack11l111_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ម"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡢࡻ࠸ࡩࠧយ"),
  bstack11l111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭រ"): bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࠪល"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭វ"): bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪឝ"),
  bstack11l111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪឞ"): bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫស"),
  bstack11l111_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ហ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠭ឡ"),
  bstack11l111_opy_ (u"ࠩࡦࡳࡳࡹ࡯࡭ࡧࡏࡳ࡬ࡹࠧអ"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡳࡹ࡯࡭ࡧࠪឣ"),
  bstack11l111_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࠩឤ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࠩឥ"),
  bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲࡒ࡯ࡨࡵࠪឦ"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡒ࡯ࡨࡵࠪឧ"),
  bstack11l111_opy_ (u"ࠨࡸ࡬ࡨࡪࡵࠧឨ"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡸ࡬ࡨࡪࡵࠧឩ"),
  bstack11l111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡑࡵࡧࡴࠩឪ"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡲࡥ࡯࡫ࡸࡱࡑࡵࡧࡴࠩឫ"),
  bstack11l111_opy_ (u"ࠬࡺࡥ࡭ࡧࡰࡩࡹࡸࡹࡍࡱࡪࡷࠬឬ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥ࡭ࡧࡰࡩࡹࡸࡹࡍࡱࡪࡷࠬឭ"),
  bstack11l111_opy_ (u"ࠧࡨࡧࡲࡐࡴࡩࡡࡵ࡫ࡲࡲࠬឮ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡨࡧࡲࡐࡴࡩࡡࡵ࡫ࡲࡲࠬឯ"),
  bstack11l111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡺࡰࡰࡨࠫឰ"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷ࡭ࡲ࡫ࡺࡰࡰࡨࠫឱ"),
  bstack11l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ឲ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧឳ"),
  bstack11l111_opy_ (u"࠭࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬ឴"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬ឵"),
  bstack11l111_opy_ (u"ࠨ࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ា"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ិ"),
  bstack11l111_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪី"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪឹ"),
  bstack11l111_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾࡹࠧឺ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡯ࡦࡎࡩࡾࡹࠧុ"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳ࡜ࡧࡩࡵࠩូ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡷࡷࡳ࡜ࡧࡩࡵࠩួ"),
  bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺࡳࠨើ"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡫ࡳࡸࡺࡳࠨឿ"),
  bstack11l111_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬៀ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧ࡬ࡣࡢࡥ࡫ࡩࠬេ"),
  bstack11l111_opy_ (u"࠭ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧែ"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧៃ"),
  bstack11l111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫោ"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫៅ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧំ"): bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫះ"),
  bstack11l111_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩៈ"): bstack11l111_opy_ (u"࠭ࡲࡦࡣ࡯ࡣࡲࡵࡢࡪ࡮ࡨࠫ៉"),
  bstack11l111_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ៊"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ់"),
  bstack11l111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡐࡨࡸࡼࡵࡲ࡬ࠩ៌"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡹࡸࡺ࡯࡮ࡐࡨࡸࡼࡵࡲ࡬ࠩ៍"),
  bstack11l111_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬ៎"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬ៏"),
  bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹࡏ࡮ࡴࡧࡦࡹࡷ࡫ࡃࡦࡴࡷࡷࠬ័"): bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࡳࠨ៑"),
  bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ្ࠪ"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ៓"),
  bstack11l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ។"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡴࡻࡲࡤࡧࠪ៕"),
  bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ៖"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧៗ"),
  bstack11l111_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦࠩ៘"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡩࡱࡶࡸࡓࡧ࡭ࡦࠩ៙"),
  bstack11l111_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡕ࡬ࡱࠬ៚"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡨࡲࡦࡨ࡬ࡦࡕ࡬ࡱࠬ៛"),
  bstack11l111_opy_ (u"ࠫࡸ࡯࡭ࡐࡲࡷ࡭ࡴࡴࡳࠨៜ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡯࡭ࡐࡲࡷ࡭ࡴࡴࡳࠨ៝"),
  bstack11l111_opy_ (u"࠭ࡵࡱ࡮ࡲࡥࡩࡓࡥࡥ࡫ࡤࠫ៞"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡱ࡮ࡲࡥࡩࡓࡥࡥ࡫ࡤࠫ៟"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ០"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ១"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ២"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ៣")
}
bstack11l1l11l1ll_opy_ = [
  bstack11l111_opy_ (u"ࠬࡵࡳࠨ៤"),
  bstack11l111_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ៥"),
  bstack11l111_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ៦"),
  bstack11l111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭៧"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭៨"),
  bstack11l111_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧ៩"),
  bstack11l111_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ៪"),
]
bstack11111l11ll_opy_ = {
  bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ៫"): [bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ៬"), bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡓࡇࡍࡆࠩ៭")],
  bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ៮"): bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ៯"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭៰"): bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠧ៱"),
  bstack11l111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ៲"): bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠫ៳"),
  bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ៴"): bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ៵"),
  bstack11l111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ៶"): bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡅࡗࡇࡌࡍࡇࡏࡗࡤࡖࡅࡓࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫ៷"),
  bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ៸"): bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࠪ៹"),
  bstack11l111_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪ៺"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ៻"),
  bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬ៼"): [bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡓࡔࡤࡏࡄࠨ៽"), bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕ࠭៾")],
  bstack11l111_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭៿"): bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡘࡊࡋࡠࡎࡒࡋࡑࡋࡖࡆࡎࠪ᠀"),
  bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᠁"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ᠂"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᠃"): [bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞࠭᠄"), bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪ᠅")],
  bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ᠆"): bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙࡛ࡒࡃࡑࡖࡇࡆࡒࡅࠨ᠇"),
  bstack11l111_opy_ (u"࠭ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࡆࡐ࡙ࠫ᠈"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡏࡓࡅࡋࡉࡘ࡚ࡒࡂࡖࡌࡓࡓࡥࡓࡎࡃࡕࡘࡤ࡙ࡅࡍࡇࡆࡘࡎࡕࡎࡠࡈࡈࡅ࡙࡛ࡒࡆࡡࡅࡖࡆࡔࡃࡉࡇࡖࠫ᠉")
}
bstack1l1111l1l1_opy_ = {
  bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᠊"): [bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ᠋"), bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ᠌")],
  bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ᠍"): [bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶࡣࡰ࡫ࡹࠨ᠎"), bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ᠏")],
  bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᠐"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᠑"),
  bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᠒"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᠓"),
  bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᠔"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᠕"),
  bstack11l111_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭᠖"): [bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡰࡱࡲࠪ᠗"), bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ᠘")],
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭᠙"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨ᠚"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨ᠛"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨ᠜"),
  bstack11l111_opy_ (u"࠭ࡡࡱࡲࠪ᠝"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲࠪ᠞"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ᠟"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᠠ"),
  bstack11l111_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᠡ"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᠢ"),
  bstack11l111_opy_ (u"ࠧࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡃࡍࡋࠥᠣ"): bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࠦᠤ"),
}
bstack1l1ll1ll11_opy_ = {
  bstack11l111_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᠥ"): bstack11l111_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᠦ"),
  bstack11l111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᠧ"): [bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᠨ"), bstack11l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᠩ")],
  bstack11l111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᠪ"): bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᠫ"),
  bstack11l111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᠬ"): bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨᠭ"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᠮ"): [bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫᠯ"), bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪᠰ")],
  bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᠱ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᠲ"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫᠳ"): bstack11l111_opy_ (u"ࠨࡴࡨࡥࡱࡥ࡭ࡰࡤ࡬ࡰࡪ࠭ᠴ"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᠵ"): [bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪᠶ"), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᠷ")],
  bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᠸ"): [bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹࡹࠧᠹ"), bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࠧᠺ")]
}
bstack11l1111l1l_opy_ = [
  bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧᠻ"),
  bstack11l111_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬᠼ"),
  bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩᠽ"),
  bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡘ࡫ࡱࡨࡴࡽࡒࡦࡥࡷࠫᠾ"),
  bstack11l111_opy_ (u"ࠬࡺࡩ࡮ࡧࡲࡹࡹࡹࠧᠿ"),
  bstack11l111_opy_ (u"࠭ࡳࡵࡴ࡬ࡧࡹࡌࡩ࡭ࡧࡌࡲࡹ࡫ࡲࡢࡥࡷࡥࡧ࡯࡬ࡪࡶࡼࠫᡀ"),
  bstack11l111_opy_ (u"ࠧࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡓࡶࡴࡳࡰࡵࡄࡨ࡬ࡦࡼࡩࡰࡴࠪᡁ"),
  bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᡂ"),
  bstack11l111_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧᡃ"),
  bstack11l111_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫᡄ"),
  bstack11l111_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᡅ"),
  bstack11l111_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᡆ"),
]
bstack11llll1l1_opy_ = [
  bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᡇ"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫᡈ"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᡉ"),
  bstack11l111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᡊ"),
  bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᡋ"),
  bstack11l111_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᡌ"),
  bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᡍ"),
  bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᡎ"),
  bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᡏ"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ᡐ"),
  bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᡑ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠪᡒ"),
  bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭ᡓ"),
  bstack11l111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡙ࡧࡧࠨᡔ"),
  bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᡕ"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᡖ"),
  bstack11l111_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᡗ"),
  bstack11l111_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠱ࠨᡘ"),
  bstack11l111_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠳ࠩᡙ"),
  bstack11l111_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠵ࠪᡚ"),
  bstack11l111_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠷ࠫᡛ"),
  bstack11l111_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠹ࠬᡜ"),
  bstack11l111_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠻࠭ᡝ"),
  bstack11l111_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠽ࠧᡞ"),
  bstack11l111_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠸ࠨᡟ"),
  bstack11l111_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠺ࠩᡠ"),
  bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᡡ"),
  bstack11l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫᡢ"),
  bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᡣ"),
  bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᡤ"),
  bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᡥ"),
  bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᡦ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᡧ")
]
bstack11l11llll11_opy_ = [
  bstack11l111_opy_ (u"ࠫࡺࡶ࡬ࡰࡣࡧࡑࡪࡪࡩࡢࠩᡨ"),
  bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᡩ"),
  bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᡪ"),
  bstack11l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᡫ"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡖࡲࡪࡱࡵ࡭ࡹࡿࠧᡬ"),
  bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᡭ"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡖࡤ࡫ࠬᡮ"),
  bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᡯ"),
  bstack11l111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᡰ"),
  bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᡱ"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᡲ"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧᡳ"),
  bstack11l111_opy_ (u"ࠩࡲࡷࠬᡴ"),
  bstack11l111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᡵ"),
  bstack11l111_opy_ (u"ࠫ࡭ࡵࡳࡵࡵࠪᡶ"),
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡥ࡮ࡺࠧᡷ"),
  bstack11l111_opy_ (u"࠭ࡲࡦࡩ࡬ࡳࡳ࠭ᡸ"),
  bstack11l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩ᡹"),
  bstack11l111_opy_ (u"ࠨ࡯ࡤࡧ࡭࡯࡮ࡦࠩ᡺"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡸࡵ࡬ࡶࡶ࡬ࡳࡳ࠭᡻"),
  bstack11l111_opy_ (u"ࠪ࡭ࡩࡲࡥࡕ࡫ࡰࡩࡴࡻࡴࠨ᡼"),
  bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡓࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨ᡽"),
  bstack11l111_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫ᡾"),
  bstack11l111_opy_ (u"࠭࡮ࡰࡒࡤ࡫ࡪࡒ࡯ࡢࡦࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᡿"),
  bstack11l111_opy_ (u"ࠧࡣࡨࡦࡥࡨ࡮ࡥࠨᢀ"),
  bstack11l111_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧᢁ"),
  bstack11l111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᢂ"),
  bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡩࡳࡪࡋࡦࡻࡶࠫᢃ"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᢄ"),
  bstack11l111_opy_ (u"ࠬࡴ࡯ࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠩᢅ"),
  bstack11l111_opy_ (u"࠭ࡣࡩࡧࡦ࡯࡚ࡘࡌࠨᢆ"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᢇ"),
  bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡄࡱࡲ࡯࡮࡫ࡳࠨᢈ"),
  bstack11l111_opy_ (u"ࠩࡦࡥࡵࡺࡵࡳࡧࡆࡶࡦࡹࡨࠨᢉ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᢊ"),
  bstack11l111_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᢋ"),
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡘࡨࡶࡸ࡯࡯࡯ࠩᢌ"),
  bstack11l111_opy_ (u"࠭࡮ࡰࡄ࡯ࡥࡳࡱࡐࡰ࡮࡯࡭ࡳ࡭ࠧᢍ"),
  bstack11l111_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡘ࡫࡮ࡥࡍࡨࡽࡸ࠭ᢎ"),
  bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡍࡱࡪࡷࠬᢏ"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡋࡧࠫᢐ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡪࡩࡤࡣࡷࡩࡩࡊࡥࡷ࡫ࡦࡩࠬᢑ"),
  bstack11l111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡔࡦࡸࡡ࡮ࡵࠪᢒ"),
  bstack11l111_opy_ (u"ࠬࡶࡨࡰࡰࡨࡒࡺࡳࡢࡦࡴࠪᢓ"),
  bstack11l111_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࠫᢔ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡔࡶࡴࡪࡱࡱࡷࠬᢕ"),
  bstack11l111_opy_ (u"ࠨࡥࡲࡲࡸࡵ࡬ࡦࡎࡲ࡫ࡸ࠭ᢖ"),
  bstack11l111_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᢗ"),
  bstack11l111_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧᢘ"),
  bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡆ࡮ࡵ࡭ࡦࡶࡵ࡭ࡨ࠭ᢙ"),
  bstack11l111_opy_ (u"ࠬࡼࡩࡥࡧࡲ࡚࠷࠭ᢚ"),
  bstack11l111_opy_ (u"࠭࡭ࡪࡦࡖࡩࡸࡹࡩࡰࡰࡌࡲࡸࡺࡡ࡭࡮ࡄࡴࡵࡹࠧᢛ"),
  bstack11l111_opy_ (u"ࠧࡦࡵࡳࡶࡪࡹࡳࡰࡕࡨࡶࡻ࡫ࡲࠨᢜ"),
  bstack11l111_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧᢝ"),
  bstack11l111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࡇࡩࡶࠧᢞ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪᢟ"),
  bstack11l111_opy_ (u"ࠫࡸࡿ࡮ࡤࡖ࡬ࡱࡪ࡝ࡩࡵࡪࡑࡘࡕ࠭ᢠ"),
  bstack11l111_opy_ (u"ࠬ࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪᢡ"),
  bstack11l111_opy_ (u"࠭ࡧࡱࡵࡏࡳࡨࡧࡴࡪࡱࡱࠫᢢ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡑࡴࡲࡪ࡮ࡲࡥࠨᢣ"),
  bstack11l111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡏࡧࡷࡻࡴࡸ࡫ࠨᢤ"),
  bstack11l111_opy_ (u"ࠩࡩࡳࡷࡩࡥࡄࡪࡤࡲ࡬࡫ࡊࡢࡴࠪᢥ"),
  bstack11l111_opy_ (u"ࠪࡼࡲࡹࡊࡢࡴࠪᢦ"),
  bstack11l111_opy_ (u"ࠫࡽࡳࡸࡋࡣࡵࠫᢧ"),
  bstack11l111_opy_ (u"ࠬࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫᢨ"),
  bstack11l111_opy_ (u"࠭࡭ࡢࡵ࡮ࡆࡦࡹࡩࡤࡃࡸࡸ࡭ᢩ࠭"),
  bstack11l111_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨᢪ"),
  bstack11l111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫ᢫"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᢬"),
  bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩ᢭"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡳࡪࡩࡱࡅࡵࡶࠧ᢮"),
  bstack11l111_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇ࡮ࡪ࡯ࡤࡸ࡮ࡵ࡮ࡴࠩ᢯"),
  bstack11l111_opy_ (u"࠭ࡣࡢࡰࡤࡶࡾ࠭ᢰ"),
  bstack11l111_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨᢱ"),
  bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨᢲ"),
  bstack11l111_opy_ (u"ࠩ࡬ࡩࠬᢳ"),
  bstack11l111_opy_ (u"ࠪࡩࡩ࡭ࡥࠨᢴ"),
  bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫᢵ"),
  bstack11l111_opy_ (u"ࠬࡷࡵࡦࡷࡨࠫᢶ"),
  bstack11l111_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨᢷ"),
  bstack11l111_opy_ (u"ࠧࡢࡲࡳࡗࡹࡵࡲࡦࡅࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠨᢸ"),
  bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡄࡣࡰࡩࡷࡧࡉ࡮ࡣࡪࡩࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧᢹ"),
  bstack11l111_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡅࡹࡥ࡯ࡹࡩ࡫ࡈࡰࡵࡷࡷࠬᢺ"),
  bstack11l111_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࡊࡰࡦࡰࡺࡪࡥࡉࡱࡶࡸࡸ࠭ᢻ"),
  bstack11l111_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡅࡵࡶࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨᢼ"),
  bstack11l111_opy_ (u"ࠬࡸࡥࡴࡧࡵࡺࡪࡊࡥࡷ࡫ࡦࡩࠬᢽ"),
  bstack11l111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᢾ"),
  bstack11l111_opy_ (u"ࠧࡴࡧࡱࡨࡐ࡫ࡹࡴࠩᢿ"),
  bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡑࡣࡶࡷࡨࡵࡤࡦࠩᣀ"),
  bstack11l111_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡋࡲࡷࡉ࡫ࡶࡪࡥࡨࡗࡪࡺࡴࡪࡰࡪࡷࠬᣁ"),
  bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡄࡹࡩ࡯࡯ࡊࡰ࡭ࡩࡨࡺࡩࡰࡰࠪᣂ"),
  bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡵࡶ࡬ࡦࡒࡤࡽࠬᣃ"),
  bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ᣄ"),
  bstack11l111_opy_ (u"࠭ࡷࡥ࡫ࡲࡗࡪࡸࡶࡪࡥࡨࠫᣅ"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᣆ"),
  bstack11l111_opy_ (u"ࠨࡲࡵࡩࡻ࡫࡮ࡵࡅࡵࡳࡸࡹࡓࡪࡶࡨࡘࡷࡧࡣ࡬࡫ࡱ࡫ࠬᣇ"),
  bstack11l111_opy_ (u"ࠩ࡫࡭࡬࡮ࡃࡰࡰࡷࡶࡦࡹࡴࠨᣈ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡓࡶࡪ࡬ࡥࡳࡧࡱࡧࡪࡹࠧᣉ"),
  bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡗ࡮ࡳࠧᣊ"),
  bstack11l111_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᣋ"),
  bstack11l111_opy_ (u"࠭ࡲࡦ࡯ࡲࡺࡪࡏࡏࡔࡃࡳࡴࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࡒ࡯ࡤࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫᣌ"),
  bstack11l111_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦࠩᣍ"),
  bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᣎ"),
  bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫᣏ"),
  bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩᣐ"),
  bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᣑ"),
  bstack11l111_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨᣒ"),
  bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬᣓ"),
  bstack11l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡴࡻࡴࡴࠩᣔ"),
  bstack11l111_opy_ (u"ࠨࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡔࡷࡵ࡭ࡱࡶࡅࡩ࡭ࡧࡶࡪࡱࡵࠫᣕ")
]
bstack11ll1l11l_opy_ = {
  bstack11l111_opy_ (u"ࠩࡹࠫᣖ"): bstack11l111_opy_ (u"ࠪࡺࠬᣗ"),
  bstack11l111_opy_ (u"ࠫ࡫࠭ᣘ"): bstack11l111_opy_ (u"ࠬ࡬ࠧᣙ"),
  bstack11l111_opy_ (u"࠭ࡦࡰࡴࡦࡩࠬᣚ"): bstack11l111_opy_ (u"ࠧࡧࡱࡵࡧࡪ࠭ᣛ"),
  bstack11l111_opy_ (u"ࠨࡱࡱࡰࡾࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᣜ"): bstack11l111_opy_ (u"ࠩࡲࡲࡱࡿࡁࡶࡶࡲࡱࡦࡺࡥࠨᣝ"),
  bstack11l111_opy_ (u"ࠪࡪࡴࡸࡣࡦ࡮ࡲࡧࡦࡲࠧᣞ"): bstack11l111_opy_ (u"ࠫ࡫ࡵࡲࡤࡧ࡯ࡳࡨࡧ࡬ࠨᣟ"),
  bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡬ࡴࡹࡴࠨᣠ"): bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩᣡ"),
  bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡶ࡯ࡳࡶࠪᣢ"): bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫᣣ"),
  bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬᣤ"): bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᣥ"),
  bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡥࡸࡹࠧᣦ"): bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨᣧ"),
  bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻ࡫ࡳࡸࡺࠧᣨ"): bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡌࡴࡹࡴࠨᣩ"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡵࡲࡵࠩᣪ"): bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᣫ"),
  bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫᣬ"): bstack11l111_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᣭ"),
  bstack11l111_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻࡸࡷࡪࡸࠧᣮ"): bstack11l111_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᣯ"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨᣰ"): bstack11l111_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪᣱ"),
  bstack11l111_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫᣲ"): bstack11l111_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬᣳ"),
  bstack11l111_opy_ (u"ࠫࡧ࡯࡮ࡢࡴࡼࡴࡦࡺࡨࠨᣴ"): bstack11l111_opy_ (u"ࠬࡨࡩ࡯ࡣࡵࡽࡵࡧࡴࡩࠩᣵ"),
  bstack11l111_opy_ (u"࠭ࡰࡢࡥࡩ࡭ࡱ࡫ࠧ᣶"): bstack11l111_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪ᣷"),
  bstack11l111_opy_ (u"ࠨࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪ᣸"): bstack11l111_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ᣹"),
  bstack11l111_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭᣺"): bstack11l111_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ᣻"),
  bstack11l111_opy_ (u"ࠬࡲ࡯ࡨࡨ࡬ࡰࡪ࠭᣼"): bstack11l111_opy_ (u"࠭࡬ࡰࡩࡩ࡭ࡱ࡫ࠧ᣽"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᣾"): bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᣿"),
  bstack11l111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫᤀ"): bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࠫᤁ")
}
bstack11l11ll11l1_opy_ = bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴࡭ࡩࡵࡪࡸࡦ࠳ࡩ࡯࡮࠱ࡳࡩࡷࡩࡹ࠰ࡥ࡯࡭࠴ࡸࡥ࡭ࡧࡤࡷࡪࡹ࠯࡭ࡣࡷࡩࡸࡺ࠯ࡥࡱࡺࡲࡱࡵࡡࡥࠤᤂ")
bstack11l1l11ll11_opy_ = bstack11l111_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠴࡮ࡥࡢ࡮ࡷ࡬ࡨ࡮ࡥࡤ࡭ࠥᤃ")
bstack11llll1l1l_opy_ = bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡦࡦࡶ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡴࡧࡱࡨࡤࡹࡤ࡬ࡡࡨࡺࡪࡴࡴࡴࠤᤄ")
bstack1l1l1l1l1_opy_ = bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡹࡧ࠳࡭ࡻࡢࠨᤅ")
bstack1l111lll1_opy_ = bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠫᤆ")
bstack11lllll1ll_opy_ = bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡲࡪࡾࡴࡠࡪࡸࡦࡸ࠭ᤇ")
bstack11l1l11l111_opy_ = {
  bstack11l111_opy_ (u"ࠪࡧࡷ࡯ࡴࡪࡥࡤࡰࠬᤈ"): 50,
  bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᤉ"): 40,
  bstack11l111_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ᤊ"): 30,
  bstack11l111_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᤋ"): 20,
  bstack11l111_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᤌ"): 10
}
bstack1llll11lll_opy_ = bstack11l1l11l111_opy_[bstack11l111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᤍ")]
bstack11llll1lll_opy_ = bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᤎ")
bstack11llll1ll_opy_ = bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨᤏ")
bstack11l1111lll_opy_ = bstack11l111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᤐ")
bstack1ll1111ll_opy_ = bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᤑ")
bstack11l11ll1_opy_ = bstack11l111_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺࠠࡢࡰࡧࠤࡵࡿࡴࡦࡵࡷ࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡰࡢࡥ࡮ࡥ࡬࡫ࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡲࡼࡸࡪࡹࡴ࠮ࡵࡨࡰࡪࡴࡩࡶ࡯ࡣࠫᤒ")
bstack11l1l11lll1_opy_ = [bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᤓ"), bstack11l111_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᤔ")]
bstack11l1l1l1l1l_opy_ = [bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᤕ"), bstack11l111_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬᤖ")]
bstack1ll1l1111_opy_ = re.compile(bstack11l111_opy_ (u"ࠫࡣࡡ࡜࡝ࡹ࠰ࡡ࠰ࡀ࠮ࠫࠦࠪᤗ"))
bstack1ll11l1l11_opy_ = [
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡐࡤࡱࡪ࠭ᤘ"),
  bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᤙ"),
  bstack11l111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᤚ"),
  bstack11l111_opy_ (u"ࠨࡰࡨࡻࡈࡵ࡭࡮ࡣࡱࡨ࡙࡯࡭ࡦࡱࡸࡸࠬᤛ"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭ᤜ"),
  bstack11l111_opy_ (u"ࠪࡹࡩ࡯ࡤࠨᤝ"),
  bstack11l111_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ᤞ"),
  bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡩࠬ᤟"),
  bstack11l111_opy_ (u"࠭࡯ࡳ࡫ࡨࡲࡹࡧࡴࡪࡱࡱࠫᤠ"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳ࡜࡫ࡢࡷ࡫ࡨࡻࠬᤡ"),
  bstack11l111_opy_ (u"ࠨࡰࡲࡖࡪࡹࡥࡵࠩᤢ"), bstack11l111_opy_ (u"ࠩࡩࡹࡱࡲࡒࡦࡵࡨࡸࠬᤣ"),
  bstack11l111_opy_ (u"ࠪࡧࡱ࡫ࡡࡳࡕࡼࡷࡹ࡫࡭ࡇ࡫࡯ࡩࡸ࠭ᤤ"),
  bstack11l111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡗ࡭ࡲ࡯࡮ࡨࡵࠪᤥ"),
  bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࡎࡲ࡫࡬࡯࡮ࡨࠩᤦ"),
  bstack11l111_opy_ (u"࠭࡯ࡵࡪࡨࡶࡆࡶࡰࡴࠩᤧ"),
  bstack11l111_opy_ (u"ࠧࡱࡴ࡬ࡲࡹࡖࡡࡨࡧࡖࡳࡺࡸࡣࡦࡑࡱࡊ࡮ࡴࡤࡇࡣ࡬ࡰࡺࡸࡥࠨᤨ"),
  bstack11l111_opy_ (u"ࠨࡣࡳࡴࡆࡩࡴࡪࡸ࡬ࡸࡾ࠭ᤩ"), bstack11l111_opy_ (u"ࠩࡤࡴࡵࡖࡡࡤ࡭ࡤ࡫ࡪ࠭ᤪ"), bstack11l111_opy_ (u"ࠪࡥࡵࡶࡗࡢ࡫ࡷࡅࡨࡺࡩࡷ࡫ࡷࡽࠬᤫ"), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡕࡧࡣ࡬ࡣࡪࡩࠬ᤬"), bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡊࡵࡳࡣࡷ࡭ࡴࡴࠧ᤭"),
  bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫ᤮"),
  bstack11l111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼ࡚ࡥࡴࡶࡓࡥࡨࡱࡡࡨࡧࡶࠫ᤯"),
  bstack11l111_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡅࡲࡺࡪࡸࡡࡨࡧࠪᤰ"), bstack11l111_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡆࡳࡻ࡫ࡲࡢࡩࡨࡉࡳࡪࡉ࡯ࡶࡨࡲࡹ࠭ᤱ"),
  bstack11l111_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡈࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨᤲ"),
  bstack11l111_opy_ (u"ࠫࡦࡪࡢࡑࡱࡵࡸࠬᤳ"),
  bstack11l111_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡊࡥࡷ࡫ࡦࡩࡘࡵࡣ࡬ࡧࡷࠫᤴ"),
  bstack11l111_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡉ࡯ࡵࡷࡥࡱࡲࡔࡪ࡯ࡨࡳࡺࡺࠧᤵ"),
  bstack11l111_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡊࡰࡶࡸࡦࡲ࡬ࡑࡣࡷ࡬ࠬᤶ"),
  bstack11l111_opy_ (u"ࠨࡣࡹࡨࠬᤷ"), bstack11l111_opy_ (u"ࠩࡤࡺࡩࡒࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬᤸ"), bstack11l111_opy_ (u"ࠪࡥࡻࡪࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸ᤹ࠬ"), bstack11l111_opy_ (u"ࠫࡦࡼࡤࡂࡴࡪࡷࠬ᤺"),
  bstack11l111_opy_ (u"ࠬࡻࡳࡦࡍࡨࡽࡸࡺ࡯ࡳࡧ᤻ࠪ"), bstack11l111_opy_ (u"࠭࡫ࡦࡻࡶࡸࡴࡸࡥࡑࡣࡷ࡬ࠬ᤼"), bstack11l111_opy_ (u"ࠧ࡬ࡧࡼࡷࡹࡵࡲࡦࡒࡤࡷࡸࡽ࡯ࡳࡦࠪ᤽"),
  bstack11l111_opy_ (u"ࠨ࡭ࡨࡽࡆࡲࡩࡢࡵࠪ᤾"), bstack11l111_opy_ (u"ࠩ࡮ࡩࡾࡖࡡࡴࡵࡺࡳࡷࡪࠧ᤿"),
  bstack11l111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࠬ᥀"), bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡄࡶ࡬ࡹࠧ᥁"), bstack11l111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࡄࡪࡴࠪ᥂"), bstack11l111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡈ࡮ࡲࡰ࡯ࡨࡑࡦࡶࡰࡪࡰࡪࡊ࡮ࡲࡥࠨ᥃"), bstack11l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷ࡛ࡳࡦࡕࡼࡷࡹ࡫࡭ࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࠫ᥄"),
  bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡐࡰࡴࡷࠫ᥅"), bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡑࡱࡵࡸࡸ࠭᥆"),
  bstack11l111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡆ࡬ࡷࡦࡨ࡬ࡦࡄࡸ࡭ࡱࡪࡃࡩࡧࡦ࡯ࠬ᥇"),
  bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࡖ࡬ࡱࡪࡵࡵࡵࠩ᥈"),
  bstack11l111_opy_ (u"ࠬ࡯࡮ࡵࡧࡱࡸࡆࡩࡴࡪࡱࡱࠫ᥉"), bstack11l111_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡉࡡࡵࡧࡪࡳࡷࡿࠧ᥊"), bstack11l111_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡆ࡭ࡣࡪࡷࠬ᥋"), bstack11l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࡌࡲࡹ࡫࡮ࡵࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᥌"),
  bstack11l111_opy_ (u"ࠩࡧࡳࡳࡺࡓࡵࡱࡳࡅࡵࡶࡏ࡯ࡔࡨࡷࡪࡺࠧ᥍"),
  bstack11l111_opy_ (u"ࠪࡹࡳ࡯ࡣࡰࡦࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬ᥎"), bstack11l111_opy_ (u"ࠫࡷ࡫ࡳࡦࡶࡎࡩࡾࡨ࡯ࡢࡴࡧࠫ᥏"),
  bstack11l111_opy_ (u"ࠬࡴ࡯ࡔ࡫ࡪࡲࠬᥐ"),
  bstack11l111_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࡛࡮ࡪ࡯ࡳࡳࡷࡺࡡ࡯ࡶ࡙࡭ࡪࡽࡳࠨᥑ"),
  bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡰࡧࡶࡴ࡯ࡤࡘࡣࡷࡧ࡭࡫ࡲࡴࠩᥒ"),
  bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᥓ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡨࡸࡥࡢࡶࡨࡇ࡭ࡸ࡯࡮ࡧࡇࡶ࡮ࡼࡥࡳࡕࡨࡷࡸ࡯࡯࡯ࡵࠪᥔ"),
  bstack11l111_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧ࡚ࡩࡧ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩᥕ"),
  bstack11l111_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡘࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡑࡣࡷ࡬ࠬᥖ"),
  bstack11l111_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰ࡙ࡰࡦࡧࡧࠫᥗ"),
  bstack11l111_opy_ (u"࠭ࡧࡱࡵࡈࡲࡦࡨ࡬ࡦࡦࠪᥘ"),
  bstack11l111_opy_ (u"ࠧࡪࡵࡋࡩࡦࡪ࡬ࡦࡵࡶࠫᥙ"),
  bstack11l111_opy_ (u"ࠨࡣࡧࡦࡊࡾࡥࡤࡖ࡬ࡱࡪࡵࡵࡵࠩᥚ"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࡕࡦࡶ࡮ࡶࡴࠨᥛ"),
  bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡅࡧࡹ࡭ࡨ࡫ࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡣࡷ࡭ࡴࡴࠧᥜ"),
  bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰࡉࡵࡥࡳࡺࡐࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠫᥝ"),
  bstack11l111_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡔࡡࡵࡷࡵࡥࡱࡕࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᥞ"),
  bstack11l111_opy_ (u"࠭ࡳࡺࡵࡷࡩࡲࡖ࡯ࡳࡶࠪᥟ"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡁࡥࡤࡋࡳࡸࡺࠧᥠ"),
  bstack11l111_opy_ (u"ࠨࡵ࡮࡭ࡵ࡛࡮࡭ࡱࡦ࡯ࠬᥡ"), bstack11l111_opy_ (u"ࠩࡸࡲࡱࡵࡣ࡬ࡖࡼࡴࡪ࠭ᥢ"), bstack11l111_opy_ (u"ࠪࡹࡳࡲ࡯ࡤ࡭ࡎࡩࡾ࠭ᥣ"),
  bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰࡎࡤࡹࡳࡩࡨࠨᥤ"),
  bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡏࡳ࡬ࡩࡡࡵࡅࡤࡴࡹࡻࡲࡦࠩᥥ"),
  bstack11l111_opy_ (u"࠭ࡵ࡯࡫ࡱࡷࡹࡧ࡬࡭ࡑࡷ࡬ࡪࡸࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨᥦ"),
  bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡘ࡫ࡱࡨࡴࡽࡁ࡯࡫ࡰࡥࡹ࡯࡯࡯ࠩᥧ"),
  bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡔࡰࡱ࡯ࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᥨ"),
  bstack11l111_opy_ (u"ࠩࡨࡲ࡫ࡵࡲࡤࡧࡄࡴࡵࡏ࡮ࡴࡶࡤࡰࡱ࠭ᥩ"),
  bstack11l111_opy_ (u"ࠪࡩࡳࡹࡵࡳࡧ࡚ࡩࡧࡼࡩࡦࡹࡶࡌࡦࡼࡥࡑࡣࡪࡩࡸ࠭ᥪ"), bstack11l111_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡶࡵࡱࡲࡰࡸࡖ࡯ࡳࡶࠪᥫ"), bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩ࡜࡫ࡢࡷ࡫ࡨࡻࡉ࡫ࡴࡢ࡫࡯ࡷࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᥬ"),
  bstack11l111_opy_ (u"࠭ࡲࡦ࡯ࡲࡸࡪࡇࡰࡱࡵࡆࡥࡨ࡮ࡥࡍ࡫ࡰ࡭ࡹ࠭ᥭ"),
  bstack11l111_opy_ (u"ࠧࡤࡣ࡯ࡩࡳࡪࡡࡳࡈࡲࡶࡲࡧࡴࠨ᥮"),
  bstack11l111_opy_ (u"ࠨࡤࡸࡲࡩࡲࡥࡊࡦࠪ᥯"),
  bstack11l111_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩᥰ"),
  bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࡘ࡫ࡲࡷ࡫ࡦࡩࡸࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ᥱ"), bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࡙ࡥࡳࡸ࡬ࡧࡪࡹࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡦࡦࠪᥲ"),
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡄࡧࡨ࡫ࡰࡵࡃ࡯ࡩࡷࡺࡳࠨᥳ"), bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡈ࡮ࡹ࡭ࡪࡵࡶࡅࡱ࡫ࡲࡵࡵࠪᥴ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡶࡐ࡮ࡨࠧ᥵"),
  bstack11l111_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡘࡧࡥࡘࡦࡶࠧ᥶"),
  bstack11l111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡋࡱ࡭ࡹ࡯ࡡ࡭ࡗࡵࡰࠬ᥷"), bstack11l111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡄࡰࡱࡵࡷࡑࡱࡳࡹࡵࡹࠧ᥸"), bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡍ࡬ࡴ࡯ࡳࡧࡉࡶࡦࡻࡤࡘࡣࡵࡲ࡮ࡴࡧࠨ᥹"), bstack11l111_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡔࡶࡥ࡯ࡎ࡬ࡲࡰࡹࡉ࡯ࡄࡤࡧࡰ࡭ࡲࡰࡷࡱࡨࠬ᥺"),
  bstack11l111_opy_ (u"࠭࡫ࡦࡧࡳࡏࡪࡿࡃࡩࡣ࡬ࡲࡸ࠭᥻"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡯ࡺࡢࡤ࡯ࡩࡘࡺࡲࡪࡰࡪࡷࡉ࡯ࡲࠨ᥼"),
  bstack11l111_opy_ (u"ࠨࡲࡵࡳࡨ࡫ࡳࡴࡃࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᥽"),
  bstack11l111_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡲࡌࡧࡼࡈࡪࡲࡡࡺࠩ᥾"),
  bstack11l111_opy_ (u"ࠪࡷ࡭ࡵࡷࡊࡑࡖࡐࡴ࡭ࠧ᥿"),
  bstack11l111_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭ᦀ"),
  bstack11l111_opy_ (u"ࠬࡽࡥࡣ࡭࡬ࡸࡗ࡫ࡳࡱࡱࡱࡷࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᦁ"), bstack11l111_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶ࡚ࡥ࡮ࡺࡔࡪ࡯ࡨࡳࡺࡺࠧᦂ"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࠪᦃ"),
  bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡵࡼࡲࡨࡋࡸࡦࡥࡸࡸࡪࡌࡲࡰ࡯ࡋࡸࡹࡶࡳࠨᦄ"),
  bstack11l111_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡆࡥࡵࡺࡵࡳࡧࠪᦅ"),
  bstack11l111_opy_ (u"ࠪࡻࡪࡨ࡫ࡪࡶࡇࡩࡧࡻࡧࡑࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᦆ"),
  bstack11l111_opy_ (u"ࠫ࡫ࡻ࡬࡭ࡅࡲࡲࡹ࡫ࡸࡵࡎ࡬ࡷࡹ࠭ᦇ"),
  bstack11l111_opy_ (u"ࠬࡽࡡࡪࡶࡉࡳࡷࡇࡰࡱࡕࡦࡶ࡮ࡶࡴࠨᦈ"),
  bstack11l111_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࡃࡰࡰࡱࡩࡨࡺࡒࡦࡶࡵ࡭ࡪࡹࠧᦉ"),
  bstack11l111_opy_ (u"ࠧࡢࡲࡳࡒࡦࡳࡥࠨᦊ"),
  bstack11l111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡕࡏࡇࡪࡸࡴࠨᦋ"),
  bstack11l111_opy_ (u"ࠩࡷࡥࡵ࡝ࡩࡵࡪࡖ࡬ࡴࡸࡴࡑࡴࡨࡷࡸࡊࡵࡳࡣࡷ࡭ࡴࡴࠧᦌ"),
  bstack11l111_opy_ (u"ࠪࡷࡨࡧ࡬ࡦࡈࡤࡧࡹࡵࡲࠨᦍ"),
  bstack11l111_opy_ (u"ࠫࡼࡪࡡࡍࡱࡦࡥࡱࡖ࡯ࡳࡶࠪᦎ"),
  bstack11l111_opy_ (u"ࠬࡹࡨࡰࡹ࡛ࡧࡴࡪࡥࡍࡱࡪࠫᦏ"),
  bstack11l111_opy_ (u"࠭ࡩࡰࡵࡌࡲࡸࡺࡡ࡭࡮ࡓࡥࡺࡹࡥࠨᦐ"),
  bstack11l111_opy_ (u"ࠧࡹࡥࡲࡨࡪࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠩᦑ"),
  bstack11l111_opy_ (u"ࠨ࡭ࡨࡽࡨ࡮ࡡࡪࡰࡓࡥࡸࡹࡷࡰࡴࡧࠫᦒ"),
  bstack11l111_opy_ (u"ࠩࡸࡷࡪࡖࡲࡦࡤࡸ࡭ࡱࡺࡗࡅࡃࠪᦓ"),
  bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡶࡦࡰࡷ࡛ࡉࡇࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠫᦔ"),
  bstack11l111_opy_ (u"ࠫࡼ࡫ࡢࡅࡴ࡬ࡺࡪࡸࡁࡨࡧࡱࡸ࡚ࡸ࡬ࠨᦕ"),
  bstack11l111_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡶ࡫ࠫᦖ"),
  bstack11l111_opy_ (u"࠭ࡵࡴࡧࡑࡩࡼ࡝ࡄࡂࠩᦗ"),
  bstack11l111_opy_ (u"ࠧࡸࡦࡤࡐࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪᦘ"), bstack11l111_opy_ (u"ࠨࡹࡧࡥࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࡕ࡫ࡰࡩࡴࡻࡴࠨᦙ"),
  bstack11l111_opy_ (u"ࠩࡻࡧࡴࡪࡥࡐࡴࡪࡍࡩ࠭ᦚ"), bstack11l111_opy_ (u"ࠪࡼࡨࡵࡤࡦࡕ࡬࡫ࡳ࡯࡮ࡨࡋࡧࠫᦛ"),
  bstack11l111_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨ࡜ࡊࡁࡃࡷࡱࡨࡱ࡫ࡉࡥࠩᦜ"),
  bstack11l111_opy_ (u"ࠬࡸࡥࡴࡧࡷࡓࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡴࡷࡓࡳࡲࡹࠨᦝ"),
  bstack11l111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡔࡪ࡯ࡨࡳࡺࡺࡳࠨᦞ"),
  bstack11l111_opy_ (u"ࠧࡸࡦࡤࡗࡹࡧࡲࡵࡷࡳࡖࡪࡺࡲࡪࡧࡶࠫᦟ"), bstack11l111_opy_ (u"ࠨࡹࡧࡥࡘࡺࡡࡳࡶࡸࡴࡗ࡫ࡴࡳࡻࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠫᦠ"),
  bstack11l111_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࡋࡥࡷࡪࡷࡢࡴࡨࡏࡪࡿࡢࡰࡣࡵࡨࠬᦡ"),
  bstack11l111_opy_ (u"ࠪࡱࡦࡾࡔࡺࡲ࡬ࡲ࡬ࡌࡲࡦࡳࡸࡩࡳࡩࡹࠨᦢ"),
  bstack11l111_opy_ (u"ࠫࡸ࡯࡭ࡱ࡮ࡨࡍࡸ࡜ࡩࡴ࡫ࡥࡰࡪࡉࡨࡦࡥ࡮ࠫᦣ"),
  bstack11l111_opy_ (u"ࠬࡻࡳࡦࡅࡤࡶࡹ࡮ࡡࡨࡧࡖࡷࡱ࠭ᦤ"),
  bstack11l111_opy_ (u"࠭ࡳࡩࡱࡸࡰࡩ࡛ࡳࡦࡕ࡬ࡲ࡬ࡲࡥࡵࡱࡱࡘࡪࡹࡴࡎࡣࡱࡥ࡬࡫ࡲࠨᦥ"),
  bstack11l111_opy_ (u"ࠧࡴࡶࡤࡶࡹࡏࡗࡅࡒࠪᦦ"),
  bstack11l111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡔࡰࡷࡦ࡬ࡎࡪࡅ࡯ࡴࡲࡰࡱ࠭ᦧ"),
  bstack11l111_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࡊ࡬ࡨࡩ࡫࡮ࡂࡲ࡬ࡔࡴࡲࡩࡤࡻࡈࡶࡷࡵࡲࠨᦨ"),
  bstack11l111_opy_ (u"ࠪࡱࡴࡩ࡫ࡍࡱࡦࡥࡹ࡯࡯࡯ࡃࡳࡴࠬᦩ"),
  bstack11l111_opy_ (u"ࠫࡱࡵࡧࡤࡣࡷࡊࡴࡸ࡭ࡢࡶࠪᦪ"), bstack11l111_opy_ (u"ࠬࡲ࡯ࡨࡥࡤࡸࡋ࡯࡬ࡵࡧࡵࡗࡵ࡫ࡣࡴࠩᦫ"),
  bstack11l111_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡉ࡫࡬ࡢࡻࡄࡨࡧ࠭᦬"),
  bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡊࡦࡏࡳࡨࡧࡴࡰࡴࡄࡹࡹࡵࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠪ᦭")
]
bstack1111lll1l_opy_ = bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡶࡲ࡯ࡳࡦࡪࠧ᦮")
bstack11lll1ll11_opy_ = [bstack11l111_opy_ (u"ࠩ࠱ࡥࡵࡱࠧ᦯"), bstack11l111_opy_ (u"ࠪ࠲ࡦࡧࡢࠨᦰ"), bstack11l111_opy_ (u"ࠫ࠳࡯ࡰࡢࠩᦱ")]
bstack1l1l1lll1l_opy_ = [bstack11l111_opy_ (u"ࠬ࡯ࡤࠨᦲ"), bstack11l111_opy_ (u"࠭ࡰࡢࡶ࡫ࠫᦳ"), bstack11l111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪᦴ"), bstack11l111_opy_ (u"ࠨࡵ࡫ࡥࡷ࡫ࡡࡣ࡮ࡨࡣ࡮ࡪࠧᦵ")]
bstack11l1lll1ll_opy_ = {
  bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᦶ"): bstack11l111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᦷ"),
  bstack11l111_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬᦸ"): bstack11l111_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᦹ"),
  bstack11l111_opy_ (u"࠭ࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫᦺ"): bstack11l111_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᦻ"),
  bstack11l111_opy_ (u"ࠨ࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᦼ"): bstack11l111_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᦽ"),
  bstack11l111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡒࡴࡹ࡯࡯࡯ࡵࠪᦾ"): bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬᦿ")
}
bstack111l1111l_opy_ = [
  bstack11l111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᧀ"),
  bstack11l111_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᧁ"),
  bstack11l111_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᧂ"),
  bstack11l111_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᧃ"),
  bstack11l111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪᧄ"),
]
bstack1lll1l11ll_opy_ = bstack11llll1l1_opy_ + bstack11l11llll11_opy_ + bstack1ll11l1l11_opy_
bstack1ll1l1ll1_opy_ = [
  bstack11l111_opy_ (u"ࠪࡢࡱࡵࡣࡢ࡮࡫ࡳࡸࡺࠤࠨᧅ"),
  bstack11l111_opy_ (u"ࠫࡣࡨࡳ࠮࡮ࡲࡧࡦࡲ࠮ࡤࡱࡰࠨࠬᧆ"),
  bstack11l111_opy_ (u"ࠬࡤ࠱࠳࠹࠱ࠫᧇ"),
  bstack11l111_opy_ (u"࠭࡞࠲࠲࠱ࠫᧈ"),
  bstack11l111_opy_ (u"ࠧ࡟࠳࠺࠶࠳࠷࡛࠷࠯࠼ࡡ࠳࠭ᧉ"),
  bstack11l111_opy_ (u"ࠨࡠ࠴࠻࠷࠴࠲࡜࠲࠰࠽ࡢ࠴ࠧ᧊"),
  bstack11l111_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠴࡝࠳࠱࠶ࡣ࠮ࠨ᧋"),
  bstack11l111_opy_ (u"ࠪࡢ࠶࠿࠲࠯࠳࠹࠼࠳࠭᧌")
]
bstack11l1l1l1ll1_opy_ = bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ᧍")
bstack11111lll11_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠱ࡹ࠵࠴࡫ࡶࡦࡰࡷࠫ᧎")
bstack111ll1ll1_opy_ = [ bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ᧏") ]
bstack1l1l1ll1l_opy_ = [ bstack11l111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭᧐") ]
bstack1l1111ll1l_opy_ = [bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ᧑")]
bstack11ll11111_opy_ = [ bstack11l111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᧒") ]
bstack1l1lllllll_opy_ = bstack11l111_opy_ (u"ࠪࡗࡉࡑࡓࡦࡶࡸࡴࠬ᧓")
bstack1l1lll111_opy_ = bstack11l111_opy_ (u"ࠫࡘࡊࡋࡕࡧࡶࡸࡆࡺࡴࡦ࡯ࡳࡸࡪࡪࠧ᧔")
bstack1111llll1_opy_ = bstack11l111_opy_ (u"࡙ࠬࡄࡌࡖࡨࡷࡹ࡙ࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠩ᧕")
bstack111111lll_opy_ = bstack11l111_opy_ (u"࠭࠴࠯࠲࠱࠴ࠬ᧖")
bstack11111111l_opy_ = [
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡋࡇࡉࡍࡇࡇࠫ᧗"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡉࡎࡇࡇࡣࡔ࡛ࡔࠨ᧘"),
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡂࡍࡑࡆࡏࡊࡊ࡟ࡃ࡛ࡢࡇࡑࡏࡅࡏࡖࠪ᧙"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡇࡗ࡛ࡔࡘࡋࡠࡅࡋࡅࡓࡍࡅࡅࠩ᧚"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐࡋࡔࡠࡐࡒࡘࡤࡉࡏࡏࡐࡈࡇ࡙ࡋࡄࠨ᧛"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡃࡍࡑࡖࡉࡉ࠭᧜"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡓࡇࡖࡉ࡙࠭᧝"),
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡔࡈࡊ࡚࡙ࡅࡅࠩ᧞"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡄࡆࡔࡘࡔࡆࡆࠪ᧟"),
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪ᧠"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡏࡃࡐࡉࡤࡔࡏࡕࡡࡕࡉࡘࡕࡌࡗࡇࡇࠫ᧡"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡃࡇࡈࡗࡋࡓࡔࡡࡌࡒ࡛ࡇࡌࡊࡆࠪ᧢"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡄࡈࡉࡘࡅࡔࡕࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨ᧣"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡘ࡚ࡔࡎࡆࡎࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧ᧤"),
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫ᧥"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤ࡙ࡏࡄࡍࡖࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨ᧦"),
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡓࡐࡅࡎࡗࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡋࡓࡘ࡚࡟ࡖࡐࡕࡉࡆࡉࡈࡂࡄࡏࡉࠬ᧧"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡑࡔࡒ࡜࡞ࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪ᧨"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡐࡄࡑࡊࡥࡎࡐࡖࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࠬ᧩"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡓࡇࡖࡓࡑ࡛ࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫ᧪"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡑࡆࡔࡄࡂࡖࡒࡖ࡞ࡥࡐࡓࡑ࡛࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬ᧫"),
]
bstack111lll111_opy_ = bstack11l111_opy_ (u"ࠧ࠯࠱ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡣࡵࡸ࡮࡬ࡡࡤࡶࡶ࠳ࠬ᧬")
bstack1111lll1ll_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪ᧭")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ᧮"), bstack11l111_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ᧯"))
bstack11l11ll111l_opy_ = bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳ࡭ࠬ᧰")
bstack11l1l11ll1l_opy_ = [ bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᧱"), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ᧲"), bstack11l111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭᧳"), bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ᧴")]
bstack11111llll_opy_ = [ bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ᧵"), bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ᧶"), bstack11l111_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ᧷"), bstack11l111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ᧸") ]
bstack1l11ll1l1_opy_ = [ bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ᧹") ]
bstack11l11lllll1_opy_ = [ bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ᧺") ]
bstack11ll111l11_opy_ = 360
bstack11ll1l1111l_opy_ = bstack11l111_opy_ (u"ࠣࡣࡳࡴ࠲ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣ᧻")
bstack11l1l111111_opy_ = bstack11l111_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳࡮ࡹࡳࡶࡧࡶࠦ᧼")
bstack11l1l11l1l1_opy_ = bstack11l111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴࡯ࡳࡴࡷࡨࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾࠨ᧽")
bstack11l11ll1ll1_opy_ = bstack11l111_opy_ (u"ࠦࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡺࡥࡴࡶࡶࠤࡦࡸࡥࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡐࡕࠣࡺࡪࡸࡳࡪࡱࡱࠤࠪࡹࠠࡢࡰࡧࠤࡦࡨ࡯ࡷࡧࠣࡪࡴࡸࠠࡂࡰࡧࡶࡴ࡯ࡤࠡࡦࡨࡺ࡮ࡩࡥࡴ࠰ࠥ᧾")
bstack11l1l1l11l1_opy_ = bstack11l111_opy_ (u"ࠧ࠷࠱࠯࠲ࠥ᧿")
bstack1l1ll1l1_opy_ = {
  bstack11l111_opy_ (u"࠭ࡐࡂࡕࡖࠫᨀ"): bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᨁ"),
  bstack11l111_opy_ (u"ࠨࡈࡄࡍࡑ࠭ᨂ"): bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᨃ"),
  bstack11l111_opy_ (u"ࠪࡗࡐࡏࡐࠨᨄ"): bstack11l111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᨅ")
}
bstack1l1l1l11ll_opy_ = [
  bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࠤᨆ"),
  bstack11l111_opy_ (u"ࠨࡧࡰࡄࡤࡧࡰࠨᨇ"),
  bstack11l111_opy_ (u"ࠢࡨࡱࡉࡳࡷࡽࡡࡳࡦࠥᨈ"),
  bstack11l111_opy_ (u"ࠣࡴࡨࡪࡷ࡫ࡳࡩࠤᨉ"),
  bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᨊ"),
  bstack11l111_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᨋ"),
  bstack11l111_opy_ (u"ࠦࡸࡻࡢ࡮࡫ࡷࡉࡱ࡫࡭ࡦࡰࡷࠦᨌ"),
  bstack11l111_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤᨍ"),
  bstack11l111_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤᨎ"),
  bstack11l111_opy_ (u"ࠢࡤ࡮ࡨࡥࡷࡋ࡬ࡦ࡯ࡨࡲࡹࠨᨏ"),
  bstack11l111_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࡴࠤᨐ"),
  bstack11l111_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵࠤᨑ"),
  bstack11l111_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࡅࡸࡿ࡮ࡤࡕࡦࡶ࡮ࡶࡴࠣᨒ"),
  bstack11l111_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥᨓ"),
  bstack11l111_opy_ (u"ࠧࡷࡵࡪࡶࠥᨔ"),
  bstack11l111_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳࡔࡰࡷࡦ࡬ࡆࡩࡴࡪࡱࡱࠦᨕ"),
  bstack11l111_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡎࡷ࡯ࡸ࡮࡚࡯ࡶࡥ࡫ࠦᨖ"),
  bstack11l111_opy_ (u"ࠣࡵ࡫ࡥࡰ࡫ࠢᨗ"),
  bstack11l111_opy_ (u"ࠤࡦࡰࡴࡹࡥࡂࡲࡳᨘࠦ")
]
bstack11l11ll1l11_opy_ = [
  bstack11l111_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤᨙ"),
  bstack11l111_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᨚ"),
  bstack11l111_opy_ (u"ࠧࡧࡵࡵࡱࠥᨛ"),
  bstack11l111_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨ᨜"),
  bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ᨝")
]
bstack1ll1111ll1_opy_ = {
  bstack11l111_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢ᨞"): [bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣ᨟")],
  bstack11l111_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᨠ"): [bstack11l111_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᨡ")],
  bstack11l111_opy_ (u"ࠧࡧࡵࡵࡱࠥᨢ"): [bstack11l111_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᨣ"), bstack11l111_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᨤ"), bstack11l111_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᨥ"), bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᨦ")],
  bstack11l111_opy_ (u"ࠥࡱࡦࡴࡵࡢ࡮ࠥᨧ"): [bstack11l111_opy_ (u"ࠦࡲࡧ࡮ࡶࡣ࡯ࠦᨨ")],
  bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᨩ"): [bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᨪ")],
}
bstack11l11ll1lll_opy_ = {
  bstack11l111_opy_ (u"ࠢࡤ࡮࡬ࡧࡰࡋ࡬ࡦ࡯ࡨࡲࡹࠨᨫ"): bstack11l111_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࠢᨬ"),
  bstack11l111_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᨭ"): bstack11l111_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᨮ"),
  bstack11l111_opy_ (u"ࠦࡸ࡫࡮ࡥࡍࡨࡽࡸ࡚࡯ࡆ࡮ࡨࡱࡪࡴࡴࠣᨯ"): bstack11l111_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࠢᨰ"),
  bstack11l111_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡄࡧࡹ࡯ࡶࡦࡇ࡯ࡩࡲ࡫࡮ࡵࠤᨱ"): bstack11l111_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࠤᨲ"),
  bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᨳ"): bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᨴ")
}
bstack1l11l1ll_opy_ = {
  bstack11l111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧᨵ"): bstack11l111_opy_ (u"ࠫࡘࡻࡩࡵࡧࠣࡗࡪࡺࡵࡱࠩᨶ"),
  bstack11l111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᨷ"): bstack11l111_opy_ (u"࠭ࡓࡶ࡫ࡷࡩ࡚ࠥࡥࡢࡴࡧࡳࡼࡴࠧᨸ"),
  bstack11l111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᨹ"): bstack11l111_opy_ (u"ࠨࡖࡨࡷࡹࠦࡓࡦࡶࡸࡴࠬᨺ"),
  bstack11l111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᨻ"): bstack11l111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡖࡨࡥࡷࡪ࡯ࡸࡰࠪᨼ")
}
bstack11l1l1l11ll_opy_ = 65536
bstack11l1l1ll11l_opy_ = bstack11l111_opy_ (u"ࠫ࠳࠴࠮࡜ࡖࡕ࡙ࡓࡉࡁࡕࡇࡇࡡࠬᨽ")
bstack11l1l1ll111_opy_ = [
      bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᨾ"), bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᨿ"), bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᩀ"), bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᩁ"), bstack11l111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫᩂ"),
      bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᩃ"), bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᩄ"), bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᩅ"), bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᩆ"),
      bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡒࡦࡳࡥࠨᩇ"), bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᩈ"), bstack11l111_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬᩉ")
    ]
bstack11l1l111lll_opy_= {
  bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᩊ"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᩋ"),
  bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᩌ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᩍ"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ᩎ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᩏ"),
  bstack11l111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᩐ"): bstack11l111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᩑ"),
  bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᩒ"): bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᩓ"),
  bstack11l111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᩔ"): bstack11l111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᩕ"),
  bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᩖ"): bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᩗ"),
  bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᩘ"): bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᩙ"),
  bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᩚ"): bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᩛ"),
  bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬᩜ"): bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ᩝ"),
  bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᩞ"): bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᩟"),
  bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪ᩠ࠫ"): bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬᩡ"),
  bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᩢ"): bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᩣ"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨᩤ"): bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩᩥ"),
  bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠬᩦ"): bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭ᩧ"),
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᩨ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᩩ"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᩪ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᩫ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᩬ"): bstack11l111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᩭ"),
  bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᩮ"): bstack11l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᩯ"),
  bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬᩰ"): bstack11l111_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᩱ"),
  bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᩲ"): bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᩳ"),
  bstack11l111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬᩴ"): bstack11l111_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭᩵"),
  bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᩶"): bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᩷"),
  bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᩸"): bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᩹"),
  bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭᩺"): bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ᩻"),
  bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᩼"): bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᩽"),
  bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᩾"): bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶ᩿ࠫ"),
  bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨ᪀"): bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩ᪁")
}
bstack11l1l11l11l_opy_ = [bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᪂"), bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ᪃")]
bstack1l111l1l11_opy_ = (bstack11l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ᪄"),)
bstack11l1l1111ll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠲ࡺ࠶࠵ࡵࡱࡦࡤࡸࡪࡥࡣ࡭࡫ࠪ᪅")
bstack11l11l1lll_opy_ = bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠰ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠯ࡷ࠳࠲࡫ࡷ࡯ࡤࡴ࠱ࠥ᪆")
bstack1l1lll111l_opy_ = bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪࡶ࡮ࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡦࡹࡨࡣࡱࡤࡶࡩ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࠢ᪇")
bstack1l1llll11_opy_ = bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠥ᪈")
class EVENTS(Enum):
  bstack11l11lll11l_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡰ࠳࠴ࡽ࠿ࡶࡲࡪࡰࡷ࠱ࡧࡻࡩ࡭ࡦ࡯࡭ࡳࡱࠧ᪉")
  bstack11l1l1ll1l_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯ࡩࡦࡴࡵࡱࠩ᪊") # final bstack11l1l1ll1l1_opy_
  bstack11l11llllll_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡶࡩࡳࡪ࡬ࡰࡩࡶࠫ᪋")
  bstack1llll111l1_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᪌") #shift post bstack11l11lll1l1_opy_
  bstack11ll111lll_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡰࡳ࡫ࡱࡸ࠲ࡨࡵࡪ࡮ࡧࡰ࡮ࡴ࡫ࠨ᪍") #shift post bstack11l11lll1l1_opy_
  bstack11l1l1l1lll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶ࡫ࡹࡧ࠭᪎") #shift
  bstack11l1l11111l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡰࡦࡴࡦࡽ࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧ᪏") #shift
  bstack111ll111ll_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠾࡭ࡻࡢ࠮࡯ࡤࡲࡦ࡭ࡥ࡮ࡧࡱࡸࠬ᪐")
  bstack1l111lll1ll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡳࡢࡸࡨ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷࠬ᪑")
  bstack111llll11l_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡥࡴ࡬ࡺࡪࡸ࠭ࡱࡧࡵࡪࡴࡸ࡭ࡴࡥࡤࡲࠬ᪒")
  bstack111l111111_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡲ࡯ࡤࡣ࡯ࠫ᪓") #shift
  bstack11111l1ll_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡥࡵࡶ࠭ࡶࡲ࡯ࡳࡦࡪࠧ᪔") #shift
  bstack11l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡤ࡫࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠭᪕")
  bstack1l11ll11l1_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡ࠲࠳ࡼ࠾࡬࡫ࡴ࠮ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠮ࡴࡨࡷࡺࡲࡴࡴ࠯ࡶࡹࡲࡳࡡࡳࡻࠪ᪖") #shift
  bstack1ll111ll11_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࠳࠴ࡽ࠿࡭ࡥࡵ࠯ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ࠯ࡵࡩࡸࡻ࡬ࡵࡵࠪ᪗") #shift
  bstack11l1l1ll1ll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿࠧ᪘") #shift
  bstack11llllllll1_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ᪙")
  bstack111l1llll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡹࡥࡴࡵ࡬ࡳࡳ࠳ࡳࡵࡣࡷࡹࡸ࠭᪚") #shift
  bstack11ll1ll1l_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺࠧ᪛")
  bstack11l1l111l11_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡲࡰࡺࡼ࠱ࡸ࡫ࡴࡶࡲࠪ᪜") #shift
  bstack111llllll1_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡳࡦࡶࡸࡴࠬ᪝")
  bstack11l1l1l1111_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡳ࡯ࡣࡳࡷ࡭ࡵࡴࠨ᪞") # not bstack11l11llll1l_opy_ in python
  bstack1llllll1ll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲ࠻ࡳࡸ࡭ࡹ࠭᪟") # used in bstack11l11ll1l1l_opy_
  bstack1l11lll111_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡪࡩࡹ࠭᪠") # used in bstack11l11ll1l1l_opy_
  bstack1l11lllll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽࡬ࡴࡵ࡫ࠨ᪡")
  bstack1ll1l11l1l_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠬ᪢")
  bstack1lll11lll1_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠬ᪣") #
  bstack11ll1l1ll1_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀ࡯࠲࠳ࡼ࠾ࡩࡸࡩࡷࡧࡵ࠱ࡹࡧ࡫ࡦࡕࡦࡶࡪ࡫࡮ࡔࡪࡲࡸࠬ᪤")
  bstack111ll1111l_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡧࡵࡧࡾࡀࡡࡶࡶࡲ࠱ࡨࡧࡰࡵࡷࡵࡩࠬ᪥")
  bstack1l1l1l111l_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡵࡩ࠲ࡺࡥࡴࡶࠪ᪦")
  bstack11l1ll1l11_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡳࡸࡺ࠭ࡵࡧࡶࡸࠬᪧ")
  bstack11l111lll1_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡷ࡫࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᪨") #shift
  bstack111llll11_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪ᪩") #shift
  bstack11l11ll11ll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱ࠰ࡧࡦࡶࡴࡶࡴࡨࠫ᪪")
  bstack11l1l1111l1_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻࡫ࡧࡰࡪ࠳ࡴࡪ࡯ࡨࡳࡺࡺࠧ᪫")
  bstack1l1ll11l1ll_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡸࡺࡡࡳࡶࠪ᪬")
  bstack11l1l111l1l_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠧ᪭")
  bstack11l1l1l111l_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡣࡩࡧࡦ࡯࠲ࡻࡰࡥࡣࡷࡩࠬ᪮")
  bstack1l1l1ll1lll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡰࡰ࠰ࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠭᪯")
  bstack1l1l1l11l11_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡱࡱ࠱ࡨࡵ࡮࡯ࡧࡦࡸࠬ᪰")
  bstack1l11llll1ll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡹࡴࡰࡲࠪ᪱")
  bstack1l11lll1lll_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡳࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࠨ᪲")
  bstack1l1l111l111_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡤࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱࠫ᪳")
  bstack11l11lll1ll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲࡊࡰ࡬ࡸࠬ᪴")
  bstack11l1l111ll1_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡩ࡭ࡳࡪࡎࡦࡣࡵࡩࡸࡺࡈࡶࡤ᪵ࠪ")
  bstack1llllll11ll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡋࡱ࡭ࡹ᪶࠭")
  bstack1lllll1l11l_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡸࡴࠨ᪷")
  bstack1l111l1llll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡈࡵ࡮ࡧ࡫ࡪ᪸ࠫ")
  bstack11l1l11llll_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡉ࡯࡯ࡨ࡬࡫᪹ࠬ")
  bstack1l1ll11ll11_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢ࡫ࡖࡩࡱ࡬ࡈࡦࡣ࡯ࡗࡹ࡫ࡰࠨ᪺")
  bstack1l1ll1l1l11_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࡬ࡗࡪࡲࡦࡉࡧࡤࡰࡌ࡫ࡴࡓࡧࡶࡹࡱࡺࠧ᪻")
  bstack1l11l1lll1l_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡇࡹࡩࡳࡺࠧ᪼")
  bstack1l11ll1l111_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡪࡹࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡆࡸࡨࡲࡹ᪽࠭")
  bstack1l11ll11111_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻࡮ࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࡊࡼࡥ࡯ࡶࠪ᪾")
  bstack11l1l1l1l11_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡨࡲࡶࡻࡥࡶࡧࡗࡩࡸࡺࡅࡷࡧࡱࡸᪿࠬ")
  bstack1lllll11l11_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺ࡯ࡱᫀࠩ")
  bstack1l1ll11l111_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡰࡰࡖࡸࡴࡶࠧ᫁")
class STAGE(Enum):
  bstack11111l1ll1_opy_ = bstack11l111_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪ᫂")
  END = bstack11l111_opy_ (u"ࠬ࡫࡮ࡥ᫃ࠩ")
  bstack1l111l11l_opy_ = bstack11l111_opy_ (u"࠭ࡳࡪࡰࡪࡰࡪ᫄࠭")
bstack11l1l11ll1_opy_ = {
  bstack11l111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧ᫅"): bstack11l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ᫆"),
  bstack11l111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭᫇"): bstack11l111_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬ᫈")
}
PLAYWRIGHT_HUB_URL = bstack11l111_opy_ (u"ࠦࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂࠨ᫉")
bstack1l111ll1l11_opy_ = 98
bstack1l111llll11_opy_ = 100
bstack1llll111l_opy_ = {
  bstack11l111_opy_ (u"ࠬࡸࡥࡳࡷࡱ᫊ࠫ"): bstack11l111_opy_ (u"࠭࠭࠮ࡴࡨࡶࡺࡴࡳࠨ᫋"),
  bstack11l111_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭ᫌ"): bstack11l111_opy_ (u"ࠨ࠯࠰ࡶࡪࡸࡵ࡯ࡵ࠰ࡨࡪࡲࡡࡺࠩᫍ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧᫎ"): 0
}
bstack11lll111l11_opy_ = bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥ᫏")
bstack11l11lll111_opy_ = bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡻࡰ࡭ࡱࡤࡨ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣ᫐")
bstack1l11ll1l1l_opy_ = bstack11l111_opy_ (u"࡚ࠧࡅࡔࡖࠣࡖࡊࡖࡏࡓࡖࡌࡒࡌࠦࡁࡏࡆࠣࡅࡓࡇࡌ࡚ࡖࡌࡇࡘࠨ᫑")