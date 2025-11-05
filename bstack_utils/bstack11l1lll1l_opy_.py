# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import json
from bstack_utils.bstack111111l11l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1111l1_opy_(object):
  bstack111111llll_opy_ = os.path.join(os.path.expanduser(bstack11111_opy_ (u"࠭ࡾࠨ´")), bstack11111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ῾"))
  bstack1llll1lllll1_opy_ = os.path.join(bstack111111llll_opy_, bstack11111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨ῿"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll1111l1_opy_ = None
  bstack11ll1l11l1_opy_ = None
  bstack1llll1llllll_opy_ = None
  bstack1lllll1111ll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11111_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫ ")):
      cls.instance = super(bstack1lllll1111l1_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111111_opy_()
    return cls.instance
  def bstack1lllll111111_opy_(self):
    try:
      with open(self.bstack1llll1lllll1_opy_, bstack11111_opy_ (u"ࠪࡶࠬ ")) as bstack1111lllll_opy_:
        bstack1llll1llll1l_opy_ = bstack1111lllll_opy_.read()
        data = json.loads(bstack1llll1llll1l_opy_)
        if bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ ") in data:
          self.bstack1lllll11111l_opy_(data[bstack11111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ ")])
        if bstack11111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ ") in data:
          self.bstack1l1lll11l_opy_(data[bstack11111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ ")])
        if bstack11111_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ ") in data:
          self.bstack1llll1llll11_opy_(data[bstack11111_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ ")])
    except:
      pass
  def bstack1llll1llll11_opy_(self, bstack1lllll1111ll_opy_):
    if bstack1lllll1111ll_opy_ != None:
      self.bstack1lllll1111ll_opy_ = bstack1lllll1111ll_opy_
  def bstack1l1lll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11111_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ "),bstack11111_opy_ (u"ࠫࠬ "))
      self.bstack1ll1111l1_opy_ = scripts.get(bstack11111_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩ "),bstack11111_opy_ (u"࠭ࠧ​"))
      self.bstack11ll1l11l1_opy_ = scripts.get(bstack11111_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫ‌"),bstack11111_opy_ (u"ࠨࠩ‍"))
      self.bstack1llll1llllll_opy_ = scripts.get(bstack11111_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧ‎"),bstack11111_opy_ (u"ࠪࠫ‏"))
  def bstack1lllll11111l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1llll1lllll1_opy_, bstack11111_opy_ (u"ࠫࡼ࠭‐")) as file:
        json.dump({
          bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢ‑"): self.commands_to_wrap,
          bstack11111_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢ‒"): {
            bstack11111_opy_ (u"ࠢࡴࡥࡤࡲࠧ–"): self.perform_scan,
            bstack11111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧ—"): self.bstack1ll1111l1_opy_,
            bstack11111_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨ―"): self.bstack11ll1l11l1_opy_,
            bstack11111_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣ‖"): self.bstack1llll1llllll_opy_
          },
          bstack11111_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣ‗"): self.bstack1lllll1111ll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥ‘").format(e))
      pass
  def bstack1llllll11l_opy_(self, command_name):
    try:
      return any(command.get(bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ’")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1lll1l_opy_ = bstack1lllll1111l1_opy_()