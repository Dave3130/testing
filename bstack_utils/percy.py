# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1lll1l1l11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l111l_opy_ import bstack11ll1ll1ll_opy_
class bstack111llll1l_opy_:
  working_dir = os.getcwd()
  bstack11ll11111_opy_ = False
  config = {}
  bstack111l1l111l1_opy_ = bstack1l1_opy_ (u"ࠫࠬἾ")
  binary_path = bstack1l1_opy_ (u"ࠬ࠭Ἷ")
  bstack11111111lll_opy_ = bstack1l1_opy_ (u"࠭ࠧὀ")
  bstack1l11lllll_opy_ = False
  bstack1lllllll1l1l_opy_ = None
  bstack1lllllllll11_opy_ = {}
  bstack1111111l111_opy_ = 300
  bstack1llllll111ll_opy_ = False
  logger = None
  bstack1llllll11lll_opy_ = False
  bstack1ll1llll1_opy_ = False
  percy_build_id = None
  bstack1111111lll1_opy_ = bstack1l1_opy_ (u"ࠧࠨὁ")
  bstack1lllllllllll_opy_ = {
    bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨὂ") : 1,
    bstack1l1_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪὃ") : 2,
    bstack1l1_opy_ (u"ࠪࡩࡩ࡭ࡥࠨὄ") : 3,
    bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫὅ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11111111l1l_opy_(self):
    bstack1lllll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠬ࠭὆")
    bstack1llllll11l1l_opy_ = sys.platform
    bstack11111111l11_opy_ = bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ὇")
    if re.match(bstack1l1_opy_ (u"ࠢࡥࡣࡵࡻ࡮ࡴࡼ࡮ࡣࡦࠤࡴࡹࠢὈ"), bstack1llllll11l1l_opy_) != None:
      bstack1lllll1ll1ll_opy_ = bstack11l1l11lll1_opy_ + bstack1l1_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡱࡶࡼ࠳ࢀࡩࡱࠤὉ")
      self.bstack1111111lll1_opy_ = bstack1l1_opy_ (u"ࠩࡰࡥࡨ࠭Ὂ")
    elif re.match(bstack1l1_opy_ (u"ࠥࡱࡸࡽࡩ࡯ࡾࡰࡷࡾࡹࡼ࡮࡫ࡱ࡫ࡼࢂࡣࡺࡩࡺ࡭ࡳࢂࡢࡤࡥࡺ࡭ࡳࢂࡷࡪࡰࡦࡩࢁ࡫࡭ࡤࡾࡺ࡭ࡳ࠹࠲ࠣὋ"), bstack1llllll11l1l_opy_) != None:
      bstack1lllll1ll1ll_opy_ = bstack11l1l11lll1_opy_ + bstack1l1_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡼ࡯࡮࠯ࡼ࡬ࡴࠧὌ")
      bstack11111111l11_opy_ = bstack1l1_opy_ (u"ࠧࡶࡥࡳࡥࡼ࠲ࡪࡾࡥࠣὍ")
      self.bstack1111111lll1_opy_ = bstack1l1_opy_ (u"࠭ࡷࡪࡰࠪ὎")
    else:
      bstack1lllll1ll1ll_opy_ = bstack11l1l11lll1_opy_ + bstack1l1_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭࡭࡫ࡱࡹࡽ࠴ࡺࡪࡲࠥ὏")
      self.bstack1111111lll1_opy_ = bstack1l1_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧὐ")
    return bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_
  def bstack1llllllll111_opy_(self):
    try:
      bstack1llllll111l1_opy_ = [os.path.join(expanduser(bstack1l1_opy_ (u"ࠤࢁࠦὑ")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪὒ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll111l1_opy_:
        if(self.bstack1llllll1llll_opy_(path)):
          return path
      raise bstack1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣὓ")
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠰ࠤࢀࢃࠢὔ").format(e))
  def bstack1llllll1llll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll11l11_opy_(self, bstack1111111l1l1_opy_):
    return os.path.join(bstack1111111l1l1_opy_, self.bstack111l1l111l1_opy_ + bstack1l1_opy_ (u"ࠨ࠮ࡦࡶࡤ࡫ࠧὕ"))
  def bstack1lllll1ll111_opy_(self, bstack1111111l1l1_opy_, bstack1111111111l_opy_):
    if not bstack1111111111l_opy_: return
    try:
      bstack1llllll11111_opy_ = self.bstack1llllll11l11_opy_(bstack1111111l1l1_opy_)
      with open(bstack1llllll11111_opy_, bstack1l1_opy_ (u"ࠢࡸࠤὖ")) as f:
        f.write(bstack1111111111l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠣࡕࡤࡺࡪࡪࠠ࡯ࡧࡺࠤࡊ࡚ࡡࡨࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠧὗ"))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡸ࡭࡫ࠠࡦࡶࡤ࡫࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤ὘").format(e))
  def bstack1lllll1lllll_opy_(self, bstack1111111l1l1_opy_):
    try:
      bstack1llllll11111_opy_ = self.bstack1llllll11l11_opy_(bstack1111111l1l1_opy_)
      if os.path.exists(bstack1llllll11111_opy_):
        with open(bstack1llllll11111_opy_, bstack1l1_opy_ (u"ࠥࡶࠧὙ")) as f:
          bstack1111111111l_opy_ = f.read().strip()
          return bstack1111111111l_opy_ if bstack1111111111l_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡋࡔࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢ὚").format(e))
  def bstack1llllll1ll11_opy_(self, bstack1111111l1l1_opy_, bstack1lllll1ll1ll_opy_):
    bstack1111111l1ll_opy_ = self.bstack1lllll1lllll_opy_(bstack1111111l1l1_opy_)
    if bstack1111111l1ll_opy_:
      try:
        bstack1lllllll1ll1_opy_ = self.bstack1lllllllll1l_opy_(bstack1111111l1ll_opy_, bstack1lllll1ll1ll_opy_)
        if not bstack1lllllll1ll1_opy_:
          self.logger.debug(bstack1l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡮ࡹࠠࡶࡲࠣࡸࡴࠦࡤࡢࡶࡨࠤ࠭ࡋࡔࡢࡩࠣࡹࡳࡩࡨࡢࡰࡪࡩࡩ࠯ࠢὛ"))
          return True
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡎࡦࡹࠣࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡻࡰࡥࡣࡷࡩࠧ὜"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡳࡷࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨὝ").format(e))
    return False
  def bstack1lllllllll1l_opy_(self, bstack1111111l1ll_opy_, bstack1lllll1ll1ll_opy_):
    try:
      headers = {
        bstack1l1_opy_ (u"ࠣࡋࡩ࠱ࡓࡵ࡮ࡦ࠯ࡐࡥࡹࡩࡨࠣ὞"): bstack1111111l1ll_opy_
      }
      response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠩࡊࡉ࡙࠭Ὗ"), bstack1lllll1ll1ll_opy_, {}, {bstack1l1_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦὠ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡧ࡭࡫ࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡷࡳࡨࡦࡺࡥࡴ࠼ࠣࡿࢂࠨὡ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1lll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
  def bstack1lllll1l1ll1_opy_(self, bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_):
    try:
      bstack1111111ll1l_opy_ = self.bstack1llllllll111_opy_()
      bstack1lllll1l1l1l_opy_ = os.path.join(bstack1111111ll1l_opy_, bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡿ࡯ࡰࠨὢ"))
      bstack1llllll1111l_opy_ = os.path.join(bstack1111111ll1l_opy_, bstack11111111l11_opy_)
      if self.bstack1llllll1ll11_opy_(bstack1111111ll1l_opy_, bstack1lllll1ll1ll_opy_): # if bstack1lllll1llll1_opy_, bstack1lllll1ll1l_opy_ bstack1111111111l_opy_ is bstack1llllll11ll1_opy_ to bstack111l1l11lll_opy_ version available (response 304)
        if os.path.exists(bstack1llllll1111l_opy_):
          self.logger.info(bstack1l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡸࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣὣ").format(bstack1llllll1111l_opy_))
          return bstack1llllll1111l_opy_
        if os.path.exists(bstack1lllll1l1l1l_opy_):
          self.logger.info(bstack1l1_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡺࡪࡲࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡸࡲࡿ࡯ࡰࡱ࡫ࡱ࡫ࠧὤ").format(bstack1lllll1l1l1l_opy_))
          return self.bstack1lllll11llll_opy_(bstack1lllll1l1l1l_opy_, bstack11111111l11_opy_)
      self.logger.info(bstack1l1_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯ࠣࡿࢂࠨὥ").format(bstack1lllll1ll1ll_opy_))
      response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠩࡊࡉ࡙࠭ὦ"), bstack1lllll1ll1ll_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllllll11ll_opy_ = response.headers.get(bstack1l1_opy_ (u"ࠥࡉ࡙ࡧࡧࠣὧ"), bstack1l1_opy_ (u"ࠦࠧὨ"))
        if bstack1lllllll11ll_opy_:
          self.bstack1lllll1ll111_opy_(bstack1111111ll1l_opy_, bstack1lllllll11ll_opy_)
        with open(bstack1lllll1l1l1l_opy_, bstack1l1_opy_ (u"ࠬࡽࡢࠨὩ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡤࡲࡩࠦࡳࡢࡸࡨࡨࠥࡧࡴࠡࡽࢀࠦὪ").format(bstack1lllll1l1l1l_opy_))
        return self.bstack1lllll11llll_opy_(bstack1lllll1l1l1l_opy_, bstack11111111l11_opy_)
      else:
        raise(bstack1l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡺࡨࡦࠢࡩ࡭ࡱ࡫࠮ࠡࡕࡷࡥࡹࡻࡳࠡࡥࡲࡨࡪࡀࠠࡼࡿࠥὫ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤὬ").format(e))
  def bstack1llllllll1ll_opy_(self, bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_):
    try:
      retry = 2
      bstack1llllll1111l_opy_ = None
      bstack1llllllll1l1_opy_ = False
      while retry > 0:
        bstack1llllll1111l_opy_ = self.bstack1lllll1l1ll1_opy_(bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_)
        bstack1llllllll1l1_opy_ = self.bstack111111l111l_opy_(bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_, bstack1llllll1111l_opy_)
        if bstack1llllllll1l1_opy_:
          break
        retry -= 1
      return bstack1llllll1111l_opy_, bstack1llllllll1l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡲࡤࡸ࡭ࠨὭ").format(e))
    return bstack1llllll1111l_opy_, False
  def bstack111111l111l_opy_(self, bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_, bstack1llllll1111l_opy_, bstack1lllllll111l_opy_ = 0):
    if bstack1lllllll111l_opy_ > 1:
      return False
    if bstack1llllll1111l_opy_ == None or os.path.exists(bstack1llllll1111l_opy_) == False:
      self.logger.warn(bstack1l1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡷ࡫ࡴࡳࡻ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣὮ"))
      return False
    bstack1lllllll1lll_opy_ = bstack1l1_opy_ (u"ࡶࠧࡤ࠮ࠫࡂࡳࡩࡷࡩࡹ࠰ࡥ࡯࡭ࠥࡢࡤࠬ࡞࠱ࡠࡩ࠱࡜࠯࡞ࡧ࠯ࠧὯ")
    command = bstack1l1_opy_ (u"ࠬࢁࡽࠡ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫὰ").format(bstack1llllll1111l_opy_)
    bstack1llllll1l1l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllllll1lll_opy_, bstack1llllll1l1l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡣࡩࡧࡦ࡯ࠥ࡬ࡡࡪ࡮ࡨࡨࠧά"))
      return False
  def bstack1lllll11llll_opy_(self, bstack1lllll1l1l1l_opy_, bstack11111111l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l1l1l_opy_)
      shutil.unpack_archive(bstack1lllll1l1l1l_opy_, working_dir)
      bstack1llllll1111l_opy_ = os.path.join(working_dir, bstack11111111l11_opy_)
      os.chmod(bstack1llllll1111l_opy_, 0o755)
      return bstack1llllll1111l_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡹࡳࢀࡩࡱࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣὲ"))
  def bstack11111111111_opy_(self):
    try:
      bstack1lllll1lll1l_opy_ = self.config.get(bstack1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧέ"))
      bstack11111111111_opy_ = bstack1lllll1lll1l_opy_ or (bstack1lllll1lll1l_opy_ is None and self.bstack11ll11111_opy_)
      if not bstack11111111111_opy_ or self.config.get(bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬὴ"), None) not in bstack11l1l11ll1l_opy_:
        return False
      self.bstack1l11lllll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧή").format(e))
  def bstack1lllll1l1l11_opy_(self):
    try:
      bstack1lllll1l1l11_opy_ = self.percy_capture_mode
      return bstack1lllll1l1l11_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾࠦࡣࡢࡲࡷࡹࡷ࡫ࠠ࡮ࡱࡧࡩ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧὶ").format(e))
  def init(self, bstack11ll11111_opy_, config, logger):
    self.bstack11ll11111_opy_ = bstack11ll11111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11111111111_opy_():
      return
    self.bstack1lllllllll11_opy_ = config.get(bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫί"), {})
    self.percy_capture_mode = config.get(bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩὸ"))
    try:
      bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_ = self.bstack11111111l1l_opy_()
      self.bstack111l1l111l1_opy_ = bstack11111111l11_opy_
      bstack1llllll1111l_opy_, bstack1llllllll1l1_opy_ = self.bstack1llllllll1ll_opy_(bstack1lllll1ll1ll_opy_, bstack11111111l11_opy_)
      if bstack1llllllll1l1_opy_:
        self.binary_path = bstack1llllll1111l_opy_
        thread = Thread(target=self.bstack1llllll1lll1_opy_)
        thread.start()
      else:
        self.bstack1llllll11lll_opy_ = True
        self.logger.error(bstack1l1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾ࠮࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡖࡥࡳࡥࡼࠦό").format(bstack1llllll1111l_opy_))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὺ").format(e))
  def bstack111111111ll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1_opy_ (u"ࠩ࡯ࡳ࡬࠭ύ"), bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰࡯ࡳ࡬࠭ὼ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1_opy_ (u"ࠦࡕࡻࡳࡩ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࡴࠢࡤࡸࠥࢁࡽࠣώ").format(logfile))
      self.bstack11111111lll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࠡࡲࡤࡸ࡭࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ὾").format(e))
  @measure(event_name=EVENTS.bstack11l1l11llll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
  def bstack1llllll1lll1_opy_(self):
    bstack1lllll1ll1l1_opy_ = self.bstack1lllll1lll11_opy_()
    if bstack1lllll1ll1l1_opy_ == None:
      self.bstack1llllll11lll_opy_ = True
      self.logger.error(bstack1l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠤ὿"))
      return False
    bstack1lllll1ll11l_opy_ = [bstack1l1_opy_ (u"ࠢࡢࡲࡳ࠾ࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠣᾀ") if self.bstack11ll11111_opy_ else bstack1l1_opy_ (u"ࠨࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠬᾁ")]
    bstack11111ll11ll_opy_ = self.bstack1llllll1ll1l_opy_()
    if bstack11111ll11ll_opy_ != None:
      bstack1lllll1ll11l_opy_.append(bstack1l1_opy_ (u"ࠤ࠰ࡧࠥࢁࡽࠣᾂ").format(bstack11111ll11ll_opy_))
    env = os.environ.copy()
    env[bstack1l1_opy_ (u"ࠥࡔࡊࡘࡃ࡚ࡡࡗࡓࡐࡋࡎࠣᾃ")] = bstack1lllll1ll1l1_opy_
    env[bstack1l1_opy_ (u"࡙ࠦࡎ࡟ࡃࡗࡌࡐࡉࡥࡕࡖࡋࡇࠦᾄ")] = os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᾅ"), bstack1l1_opy_ (u"࠭ࠧᾆ"))
    bstack1llllllll11l_opy_ = [self.binary_path]
    self.bstack111111111ll_opy_()
    self.bstack1lllllll1l1l_opy_ = self.bstack1111111l11l_opy_(bstack1llllllll11l_opy_ + bstack1lllll1ll11l_opy_, env)
    self.logger.debug(bstack1l1_opy_ (u"ࠢࡔࡶࡤࡶࡹ࡯࡮ࡨࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠣᾇ"))
    bstack1lllllll111l_opy_ = 0
    while self.bstack1lllllll1l1l_opy_.poll() == None:
      bstack1111111ll11_opy_ = self.bstack1llllllllll1_opy_()
      if bstack1111111ll11_opy_:
        self.logger.debug(bstack1l1_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠦᾈ"))
        self.bstack1llllll111ll_opy_ = True
        return True
      bstack1lllllll111l_opy_ += 1
      self.logger.debug(bstack1l1_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡔࡨࡸࡷࡿࠠ࠮ࠢࡾࢁࠧᾉ").format(bstack1lllllll111l_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡋࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࠦࡡࡵࡶࡨࡱࡵࡺࡳࠣᾊ").format(bstack1lllllll111l_opy_))
    self.bstack1llllll11lll_opy_ = True
    return False
  def bstack1llllllllll1_opy_(self, bstack1lllllll111l_opy_ = 0):
    if bstack1lllllll111l_opy_ > 10:
      return False
    try:
      bstack1lllll1l11l1_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡗࡊࡘࡖࡆࡔࡢࡅࡉࡊࡒࡆࡕࡖࠫᾋ"), bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡲ࡯ࡤࡣ࡯࡬ࡴࡹࡴ࠻࠷࠶࠷࠽࠭ᾌ"))
      bstack1lllllll1111_opy_ = bstack1lllll1l11l1_opy_ + bstack11l11lll11l_opy_
      response = requests.get(bstack1lllllll1111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࠬᾍ"), {}).get(bstack1l1_opy_ (u"ࠧࡪࡦࠪᾎ"), None)
      return True
    except:
      self.logger.debug(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷࡸࡥࡥࠢࡺ࡬࡮ࡲࡥࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢ࡮ࡷ࡬ࠥࡩࡨࡦࡥ࡮ࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨᾏ"))
      return False
  def bstack1lllll1lll11_opy_(self):
    bstack111111l1111_opy_ = bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠭ᾐ") if self.bstack11ll11111_opy_ else bstack1l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᾑ")
    bstack11111111ll1_opy_ = bstack1l1_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢᾒ") if self.config.get(bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᾓ")) is None else True
    bstack11ll11l11l1_opy_ = bstack1l1_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠫࡶࡥࡳࡥࡼࡁࢀࢃࠢᾔ").format(self.config[bstack1l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᾕ")], bstack111111l1111_opy_, bstack11111111ll1_opy_)
    if self.percy_capture_mode:
      bstack11ll11l11l1_opy_ += bstack1l1_opy_ (u"ࠣࠨࡳࡩࡷࡩࡹࡠࡥࡤࡴࡹࡻࡲࡦࡡࡰࡳࡩ࡫࠽ࡼࡿࠥᾖ").format(self.percy_capture_mode)
    uri = bstack11ll1ll1ll_opy_(bstack11ll11l11l1_opy_)
    try:
      response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠩࡊࡉ࡙࠭ᾗ"), uri, {}, {bstack1l1_opy_ (u"ࠪࡥࡺࡺࡨࠨᾘ"): (self.config[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᾙ")], self.config[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᾚ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11lllll_opy_ = data.get(bstack1l1_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᾛ"))
        self.percy_capture_mode = data.get(bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࠬᾜ"))
        os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᾝ")] = str(self.bstack1l11lllll_opy_)
        os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᾞ")] = str(self.percy_capture_mode)
        if bstack11111111ll1_opy_ == bstack1l1_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾟ") and str(self.bstack1l11lllll_opy_).lower() == bstack1l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᾠ"):
          self.bstack1ll1llll1_opy_ = True
        if bstack1l1_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾡ") in data:
          return data[bstack1l1_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᾢ")]
        else:
          raise bstack1l1_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᾣ").format(data)
      else:
        raise bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᾤ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᾥ").format(e))
  def bstack1llllll1ll1l_opy_(self):
    bstack1lllllll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᾦ"))
    try:
      if bstack1l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾧ") not in self.bstack1lllllllll11_opy_:
        self.bstack1lllllllll11_opy_[bstack1l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᾨ")] = 2
      with open(bstack1lllllll11l1_opy_, bstack1l1_opy_ (u"࠭ࡷࠨᾩ")) as fp:
        json.dump(self.bstack1lllllllll11_opy_, fp)
      return bstack1lllllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾪ").format(e))
  def bstack1111111l11l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111111lll1_opy_ == bstack1l1_opy_ (u"ࠨࡹ࡬ࡲࠬᾫ"):
        bstack1llllll1l111_opy_ = [bstack1l1_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᾬ"), bstack1l1_opy_ (u"ࠪ࠳ࡨ࠭ᾭ")]
        cmd = bstack1llllll1l111_opy_ + cmd
      cmd = bstack1l1_opy_ (u"ࠫࠥ࠭ᾮ").join(cmd)
      self.logger.debug(bstack1l1_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᾯ").format(cmd))
      with open(self.bstack11111111lll_opy_, bstack1l1_opy_ (u"ࠨࡡࠣᾰ")) as bstack111111111l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111111111l1_opy_, text=True, stderr=bstack111111111l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll11lll_opy_ = True
      self.logger.error(bstack1l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᾱ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll111ll_opy_:
        self.logger.info(bstack1l1_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᾲ"))
        cmd = [self.binary_path, bstack1l1_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᾳ")]
        self.bstack1111111l11l_opy_(cmd)
        self.bstack1llllll111ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᾴ").format(cmd, e))
  def bstack1ll11111ll_opy_(self):
    if not self.bstack1l11lllll_opy_:
      return
    try:
      bstack1lllll1l1lll_opy_ = 0
      while not self.bstack1llllll111ll_opy_ and bstack1lllll1l1lll_opy_ < self.bstack1111111l111_opy_:
        if self.bstack1llllll11lll_opy_:
          self.logger.info(bstack1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤ᾵"))
          return
        time.sleep(1)
        bstack1lllll1l1lll_opy_ += 1
      os.environ[bstack1l1_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᾶ")] = str(self.bstack1lllll1l111l_opy_())
      self.logger.info(bstack1l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᾷ"))
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾸ").format(e))
  def bstack1lllll1l111l_opy_(self):
    if self.bstack11ll11111_opy_:
      return
    try:
      bstack1llllll1l1ll_opy_ = [platform[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭Ᾱ")].lower() for platform in self.config.get(bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᾺ"), [])]
      bstack1llllll1l11l_opy_ = sys.maxsize
      bstack1lllll1l11ll_opy_ = bstack1l1_opy_ (u"ࠪࠫΆ")
      for browser in bstack1llllll1l1ll_opy_:
        if browser in self.bstack1lllllllllll_opy_:
          bstack1lllllll1l11_opy_ = self.bstack1lllllllllll_opy_[browser]
        if bstack1lllllll1l11_opy_ < bstack1llllll1l11l_opy_:
          bstack1llllll1l11l_opy_ = bstack1lllllll1l11_opy_
          bstack1lllll1l11ll_opy_ = browser
      return bstack1lllll1l11ll_opy_
    except Exception as e:
      self.logger.error(bstack1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾼ").format(e))
  @classmethod
  def bstack1l11l11l1l_opy_(self):
    return os.getenv(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪ᾽"), bstack1l1_opy_ (u"࠭ࡆࡢ࡮ࡶࡩࠬι")).lower()
  @classmethod
  def bstack111ll1l111_opy_(self):
    return os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫ᾿"), bstack1l1_opy_ (u"ࠨࠩ῀"))
  @classmethod
  def bstack11lllll1ll1_opy_(cls, value):
    cls.bstack1ll1llll1_opy_ = value
  @classmethod
  def bstack1lllll1l1111_opy_(cls):
    return cls.bstack1ll1llll1_opy_
  @classmethod
  def bstack11lllll11l1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1111111llll_opy_(cls):
    return cls.percy_build_id