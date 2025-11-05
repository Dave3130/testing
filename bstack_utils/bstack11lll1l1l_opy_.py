# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import json
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1111l1_opy_(object):
  bstack1l111lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠧࡿࠩ῾")), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ῿"))
  bstack1lllll11111l_opy_ = os.path.join(bstack1l111lll11_opy_, bstack11ll1ll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩ "))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1ll11l1_opy_ = None
  bstack11l1ll111_opy_ = None
  bstack1llll1lllll1_opy_ = None
  bstack1llll1llll11_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬ ")):
      cls.instance = super(bstack1lllll1111l1_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111111_opy_()
    return cls.instance
  def bstack1lllll111111_opy_(self):
    try:
      with open(self.bstack1lllll11111l_opy_, bstack11ll1ll_opy_ (u"ࠫࡷ࠭ ")) as bstack1l11lllll1_opy_:
        bstack1llll1llll1l_opy_ = bstack1l11lllll1_opy_.read()
        data = json.loads(bstack1llll1llll1l_opy_)
        if bstack11ll1ll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ ") in data:
          self.bstack1lllll1111ll_opy_(data[bstack11ll1ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ ")])
        if bstack11ll1ll_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ ") in data:
          self.bstack1ll11lllll_opy_(data[bstack11ll1ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ ")])
        if bstack11ll1ll_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ ") in data:
          self.bstack1llll1llllll_opy_(data[bstack11ll1ll_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ ")])
    except:
      pass
  def bstack1llll1llllll_opy_(self, bstack1llll1llll11_opy_):
    if bstack1llll1llll11_opy_ != None:
      self.bstack1llll1llll11_opy_ = bstack1llll1llll11_opy_
  def bstack1ll11lllll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11ll1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ "),bstack11ll1ll_opy_ (u"ࠬ࠭ "))
      self.bstack1l1ll11l1_opy_ = scripts.get(bstack11ll1ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪ​"),bstack11ll1ll_opy_ (u"ࠧࠨ‌"))
      self.bstack11l1ll111_opy_ = scripts.get(bstack11ll1ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬ‍"),bstack11ll1ll_opy_ (u"ࠩࠪ‎"))
      self.bstack1llll1lllll1_opy_ = scripts.get(bstack11ll1ll_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨ‏"),bstack11ll1ll_opy_ (u"ࠫࠬ‐"))
  def bstack1lllll1111ll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11111l_opy_, bstack11ll1ll_opy_ (u"ࠬࡽࠧ‑")) as file:
        json.dump({
          bstack11ll1ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣ‒"): self.commands_to_wrap,
          bstack11ll1ll_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣ–"): {
            bstack11ll1ll_opy_ (u"ࠣࡵࡦࡥࡳࠨ—"): self.perform_scan,
            bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨ―"): self.bstack1l1ll11l1_opy_,
            bstack11ll1ll_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢ‖"): self.bstack11l1ll111_opy_,
            bstack11ll1ll_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤ‗"): self.bstack1llll1lllll1_opy_
          },
          bstack11ll1ll_opy_ (u"ࠧࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠤ‘"): self.bstack1llll1llll11_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠺ࠡࡽࢀࠦ’").format(e))
      pass
  def bstack11l111l1ll_opy_(self, command_name):
    try:
      return any(command.get(bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ‚")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11lll1l1l_opy_ = bstack1lllll1111l1_opy_()