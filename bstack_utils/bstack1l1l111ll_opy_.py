# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
import json
from bstack_utils.bstack1l11111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1111ll_opy_(object):
  bstack11lllll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"࠭ࡾࠨῨ")), bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧῩ"))
  bstack1lllll1111l1_opy_ = os.path.join(bstack11lllll1l1_opy_, bstack11ll1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨῪ"))
  commands_to_wrap = None
  perform_scan = None
  bstack11l11l1l1l_opy_ = None
  bstack1111l11l1l_opy_ = None
  bstack1lllll11111l_opy_ = None
  bstack1lllll111ll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫΎ")):
      cls.instance = super(bstack1lllll1111ll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111l11_opy_()
    return cls.instance
  def bstack1lllll111l11_opy_(self):
    try:
      with open(self.bstack1lllll1111l1_opy_, bstack11ll1l_opy_ (u"ࠪࡶࠬῬ")) as bstack1l11ll1ll_opy_:
        bstack1lllll111lll_opy_ = bstack1l11ll1ll_opy_.read()
        data = json.loads(bstack1lllll111lll_opy_)
        if bstack11ll1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭῭") in data:
          self.bstack1lllll111l1l_opy_(data[bstack11ll1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ΅")])
        if bstack11ll1l_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ`") in data:
          self.bstack111lll11l_opy_(data[bstack11ll1l_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ῰")])
        if bstack11ll1l_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ῱") in data:
          self.bstack1lllll11l111_opy_(data[bstack11ll1l_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ῲ")])
    except:
      pass
  def bstack1lllll11l111_opy_(self, bstack1lllll111ll1_opy_):
    if bstack1lllll111ll1_opy_ != None:
      self.bstack1lllll111ll1_opy_ = bstack1lllll111ll1_opy_
  def bstack111lll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11ll1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨῳ"),bstack11ll1l_opy_ (u"ࠫࠬῴ"))
      self.bstack11l11l1l1l_opy_ = scripts.get(bstack11ll1l_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩ῵"),bstack11ll1l_opy_ (u"࠭ࠧῶ"))
      self.bstack1111l11l1l_opy_ = scripts.get(bstack11ll1l_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫῷ"),bstack11ll1l_opy_ (u"ࠨࠩῸ"))
      self.bstack1lllll11111l_opy_ = scripts.get(bstack11ll1l_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧΌ"),bstack11ll1l_opy_ (u"ࠪࠫῺ"))
  def bstack1lllll111l1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1111l1_opy_, bstack11ll1l_opy_ (u"ࠫࡼ࠭Ώ")) as file:
        json.dump({
          bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢῼ"): self.commands_to_wrap,
          bstack11ll1l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢ´"): {
            bstack11ll1l_opy_ (u"ࠢࡴࡥࡤࡲࠧ῾"): self.perform_scan,
            bstack11ll1l_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧ῿"): self.bstack11l11l1l1l_opy_,
            bstack11ll1l_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨ "): self.bstack1111l11l1l_opy_,
            bstack11ll1l_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣ "): self.bstack1lllll11111l_opy_
          },
          bstack11ll1l_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣ "): self.bstack1lllll111ll1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥ ").format(e))
      pass
  def bstack1111llllll_opy_(self, command_name):
    try:
      return any(command.get(bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l1l111ll_opy_ = bstack1lllll1111ll_opy_()