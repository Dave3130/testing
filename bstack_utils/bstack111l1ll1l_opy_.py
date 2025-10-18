# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
from bstack_utils.bstack11l111l1ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11l111_opy_(object):
  bstack11l1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨῌ")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ῍"))
  bstack1lllll11ll11_opy_ = os.path.join(bstack11l1l1ll11_opy_, bstack11l111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨ῎"))
  commands_to_wrap = None
  perform_scan = None
  bstack11ll1ll1ll_opy_ = None
  bstack1l111111ll_opy_ = None
  bstack1lllll111lll_opy_ = None
  bstack1lllll11l1ll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l111_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫ῏")):
      cls.instance = super(bstack1lllll11l111_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111l1l_opy_()
    return cls.instance
  def bstack1lllll111l1l_opy_(self):
    try:
      with open(self.bstack1lllll11ll11_opy_, bstack11l111_opy_ (u"ࠪࡶࠬῐ")) as bstack1lllll1111_opy_:
        bstack1lllll111ll1_opy_ = bstack1lllll1111_opy_.read()
        data = json.loads(bstack1lllll111ll1_opy_)
        if bstack11l111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ῑ") in data:
          self.bstack1lllll11l11l_opy_(data[bstack11l111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧῒ")])
        if bstack11l111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧΐ") in data:
          self.bstack1l1l1lll1_opy_(data[bstack11l111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ῔")])
        if bstack11l111_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ῕") in data:
          self.bstack1lllll11l1l1_opy_(data[bstack11l111_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ῖ")])
    except:
      pass
  def bstack1lllll11l1l1_opy_(self, bstack1lllll11l1ll_opy_):
    if bstack1lllll11l1ll_opy_ != None:
      self.bstack1lllll11l1ll_opy_ = bstack1lllll11l1ll_opy_
  def bstack1l1l1lll1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l111_opy_ (u"ࠪࡷࡨࡧ࡮ࠨῗ"),bstack11l111_opy_ (u"ࠫࠬῘ"))
      self.bstack11ll1ll1ll_opy_ = scripts.get(bstack11l111_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩῙ"),bstack11l111_opy_ (u"࠭ࠧῚ"))
      self.bstack1l111111ll_opy_ = scripts.get(bstack11l111_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫΊ"),bstack11l111_opy_ (u"ࠨࠩ῜"))
      self.bstack1lllll111lll_opy_ = scripts.get(bstack11l111_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧ῝"),bstack11l111_opy_ (u"ࠪࠫ῞"))
  def bstack1lllll11l11l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11ll11_opy_, bstack11l111_opy_ (u"ࠫࡼ࠭῟")) as file:
        json.dump({
          bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢῠ"): self.commands_to_wrap,
          bstack11l111_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢῡ"): {
            bstack11l111_opy_ (u"ࠢࡴࡥࡤࡲࠧῢ"): self.perform_scan,
            bstack11l111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧΰ"): self.bstack11ll1ll1ll_opy_,
            bstack11l111_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨῤ"): self.bstack1l111111ll_opy_,
            bstack11l111_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣῥ"): self.bstack1lllll111lll_opy_
          },
          bstack11l111_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣῦ"): self.bstack1lllll11l1ll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥῧ").format(e))
      pass
  def bstack11lll11ll1_opy_(self, command_name):
    try:
      return any(command.get(bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫῨ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack111l1ll1l_opy_ = bstack1lllll11l111_opy_()