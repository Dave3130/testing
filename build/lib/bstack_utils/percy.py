# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
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
from bstack_utils.helper import bstack11l1lllll1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1ll1ll1_opy_ import bstack11llllll11_opy_
class bstack111l111ll_opy_:
  working_dir = os.getcwd()
  bstack1llll1l11l_opy_ = False
  config = {}
  bstack1111ll1l111_opy_ = bstack1l111ll_opy_ (u"ࠪࠫὄ")
  binary_path = bstack1l111ll_opy_ (u"ࠫࠬὅ")
  bstack1llllll1llll_opy_ = bstack1l111ll_opy_ (u"ࠬ࠭὆")
  bstack1l11ll1l1l_opy_ = False
  bstack1lllllll1ll1_opy_ = None
  bstack1lllll1llll1_opy_ = {}
  bstack1111111ll1l_opy_ = 300
  bstack1111111111l_opy_ = False
  logger = None
  bstack1lllll11ll11_opy_ = False
  bstack1ll1l1l111_opy_ = False
  percy_build_id = None
  bstack1llllll1l1ll_opy_ = bstack1l111ll_opy_ (u"࠭ࠧ὇")
  bstack11111111l11_opy_ = {
    bstack1l111ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧὈ") : 1,
    bstack1l111ll_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩὉ") : 2,
    bstack1l111ll_opy_ (u"ࠩࡨࡨ࡬࡫ࠧὊ") : 3,
    bstack1l111ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪὋ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1llllll111l1_opy_(self):
    bstack11111111111_opy_ = bstack1l111ll_opy_ (u"ࠫࠬὌ")
    bstack1lllllll1111_opy_ = sys.platform
    bstack1lllll11l1ll_opy_ = bstack1l111ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫὍ")
    if re.match(bstack1l111ll_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨ὎"), bstack1lllllll1111_opy_) != None:
      bstack11111111111_opy_ = bstack11l11ll1l11_opy_ + bstack1l111ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣ὏")
      self.bstack1llllll1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠨ࡯ࡤࡧࠬὐ")
    elif re.match(bstack1l111ll_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢὑ"), bstack1lllllll1111_opy_) != None:
      bstack11111111111_opy_ = bstack11l11ll1l11_opy_ + bstack1l111ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦὒ")
      bstack1lllll11l1ll_opy_ = bstack1l111ll_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢὓ")
      self.bstack1llllll1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠬࡽࡩ࡯ࠩὔ")
    else:
      bstack11111111111_opy_ = bstack11l11ll1l11_opy_ + bstack1l111ll_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤὕ")
      self.bstack1llllll1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ὖ")
    return bstack11111111111_opy_, bstack1lllll11l1ll_opy_
  def bstack1lllllllll1l_opy_(self):
    try:
      bstack1111111l11l_opy_ = [os.path.join(expanduser(bstack1l111ll_opy_ (u"ࠣࢀࠥὗ")), bstack1l111ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ὘")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111111l11l_opy_:
        if(self.bstack1lllll11ll1l_opy_(path)):
          return path
      raise bstack1l111ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢὙ")
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨ὚").format(e))
  def bstack1lllll11ll1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll1l11l_opy_(self, bstack1lllll1lll1l_opy_):
    return os.path.join(bstack1lllll1lll1l_opy_, self.bstack1111ll1l111_opy_ + bstack1l111ll_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦὛ"))
  def bstack1lllllllllll_opy_(self, bstack1lllll1lll1l_opy_, bstack1lllll1l11l1_opy_):
    if not bstack1lllll1l11l1_opy_: return
    try:
      bstack1llllllll1ll_opy_ = self.bstack1llllll1l11l_opy_(bstack1lllll1lll1l_opy_)
      with open(bstack1llllllll1ll_opy_, bstack1l111ll_opy_ (u"ࠨࡷࠣ὜")) as f:
        f.write(bstack1lllll1l11l1_opy_)
        self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦὝ"))
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ὞").format(e))
  def bstack1llllll11l1l_opy_(self, bstack1lllll1lll1l_opy_):
    try:
      bstack1llllllll1ll_opy_ = self.bstack1llllll1l11l_opy_(bstack1lllll1lll1l_opy_)
      if os.path.exists(bstack1llllllll1ll_opy_):
        with open(bstack1llllllll1ll_opy_, bstack1l111ll_opy_ (u"ࠤࡵࠦὟ")) as f:
          bstack1lllll1l11l1_opy_ = f.read().strip()
          return bstack1lllll1l11l1_opy_ if bstack1lllll1l11l1_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὠ").format(e))
  def bstack1lllll1ll1l1_opy_(self, bstack1lllll1lll1l_opy_, bstack11111111111_opy_):
    bstack1lllllll111l_opy_ = self.bstack1llllll11l1l_opy_(bstack1lllll1lll1l_opy_)
    if bstack1lllllll111l_opy_:
      try:
        bstack1lllllll11ll_opy_ = self.bstack1llllll1l111_opy_(bstack1lllllll111l_opy_, bstack11111111111_opy_)
        if not bstack1lllllll11ll_opy_:
          self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨὡ"))
          return True
        self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦὢ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l111ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧὣ").format(e))
    return False
  def bstack1llllll1l111_opy_(self, bstack1lllllll111l_opy_, bstack11111111111_opy_):
    try:
      headers = {
        bstack1l111ll_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢὤ"): bstack1lllllll111l_opy_
      }
      response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠨࡉࡈࡘࠬὥ"), bstack11111111111_opy_, {}, {bstack1l111ll_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥὦ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l111ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧὧ").format(e))
  @measure(event_name=EVENTS.bstack11l11llll1l_opy_, stage=STAGE.bstack1ll11l111l_opy_)
  def bstack1lllll1ll111_opy_(self, bstack11111111111_opy_, bstack1lllll11l1ll_opy_):
    try:
      bstack111111111ll_opy_ = self.bstack1lllllllll1l_opy_()
      bstack1lllll1l111l_opy_ = os.path.join(bstack111111111ll_opy_, bstack1l111ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧὨ"))
      bstack111111111l1_opy_ = os.path.join(bstack111111111ll_opy_, bstack1lllll11l1ll_opy_)
      if self.bstack1lllll1ll1l1_opy_(bstack111111111ll_opy_, bstack11111111111_opy_): # if bstack1lllll1ll11l_opy_, bstack1lllll1l1ll_opy_ bstack1lllll1l11l1_opy_ is bstack1lllll1lllll_opy_ to bstack1111l1ll111_opy_ version available (response 304)
        if os.path.exists(bstack111111111l1_opy_):
          self.logger.info(bstack1l111ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὩ").format(bstack111111111l1_opy_))
          return bstack111111111l1_opy_
        if os.path.exists(bstack1lllll1l111l_opy_):
          self.logger.info(bstack1l111ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦὪ").format(bstack1lllll1l111l_opy_))
          return self.bstack1111111l111_opy_(bstack1lllll1l111l_opy_, bstack1lllll11l1ll_opy_)
      self.logger.info(bstack1l111ll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧὫ").format(bstack11111111111_opy_))
      response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠨࡉࡈࡘࠬὬ"), bstack11111111111_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllll1ll11_opy_ = response.headers.get(bstack1l111ll_opy_ (u"ࠤࡈࡘࡦ࡭ࠢὭ"), bstack1l111ll_opy_ (u"ࠥࠦὮ"))
        if bstack1llllll1ll11_opy_:
          self.bstack1lllllllllll_opy_(bstack111111111ll_opy_, bstack1llllll1ll11_opy_)
        with open(bstack1lllll1l111l_opy_, bstack1l111ll_opy_ (u"ࠫࡼࡨࠧὯ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l111ll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥὰ").format(bstack1lllll1l111l_opy_))
        return self.bstack1111111l111_opy_(bstack1lllll1l111l_opy_, bstack1lllll11l1ll_opy_)
      else:
        raise(bstack1l111ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤά").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣὲ").format(e))
  def bstack1llllll1ll1l_opy_(self, bstack11111111111_opy_, bstack1lllll11l1ll_opy_):
    try:
      retry = 2
      bstack111111111l1_opy_ = None
      bstack1lllll1ll1ll_opy_ = False
      while retry > 0:
        bstack111111111l1_opy_ = self.bstack1lllll1ll111_opy_(bstack11111111111_opy_, bstack1lllll11l1ll_opy_)
        bstack1lllll1ll1ll_opy_ = self.bstack1llllll1l1l1_opy_(bstack11111111111_opy_, bstack1lllll11l1ll_opy_, bstack111111111l1_opy_)
        if bstack1lllll1ll1ll_opy_:
          break
        retry -= 1
      return bstack111111111l1_opy_, bstack1lllll1ll1ll_opy_
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧέ").format(e))
    return bstack111111111l1_opy_, False
  def bstack1llllll1l1l1_opy_(self, bstack11111111111_opy_, bstack1lllll11l1ll_opy_, bstack111111111l1_opy_, bstack1llllll11lll_opy_ = 0):
    if bstack1llllll11lll_opy_ > 1:
      return False
    if bstack111111111l1_opy_ == None or os.path.exists(bstack111111111l1_opy_) == False:
      self.logger.warn(bstack1l111ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὴ"))
      return False
    bstack1111111ll11_opy_ = bstack1l111ll_opy_ (u"ࡵࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬ࠤࡡࡪࠫ࡝࠰࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࠦή")
    command = bstack1l111ll_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪὶ").format(bstack111111111l1_opy_)
    bstack1lllll1lll11_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111111ll11_opy_, bstack1lllll1lll11_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l111ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦί"))
      return False
  def bstack1111111l111_opy_(self, bstack1lllll1l111l_opy_, bstack1lllll11l1ll_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l111l_opy_)
      shutil.unpack_archive(bstack1lllll1l111l_opy_, working_dir)
      bstack111111111l1_opy_ = os.path.join(working_dir, bstack1lllll11l1ll_opy_)
      os.chmod(bstack111111111l1_opy_, 0o755)
      return bstack111111111l1_opy_
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢὸ"))
  def bstack1lllll11llll_opy_(self):
    try:
      bstack1llllllll111_opy_ = self.config.get(bstack1l111ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ό"))
      bstack1lllll11llll_opy_ = bstack1llllllll111_opy_ or (bstack1llllllll111_opy_ is None and self.bstack1llll1l11l_opy_)
      if not bstack1lllll11llll_opy_ or self.config.get(bstack1l111ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫὺ"), None) not in bstack11l11ll11ll_opy_:
        return False
      self.bstack1l11ll1l1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦύ").format(e))
  def bstack1lllllll11l1_opy_(self):
    try:
      bstack1lllllll11l1_opy_ = self.percy_capture_mode
      return bstack1lllllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦὼ").format(e))
  def init(self, bstack1llll1l11l_opy_, config, logger):
    self.bstack1llll1l11l_opy_ = bstack1llll1l11l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll11llll_opy_():
      return
    self.bstack1lllll1llll1_opy_ = config.get(bstack1l111ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪώ"), {})
    self.percy_capture_mode = config.get(bstack1l111ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨ὾"))
    try:
      bstack11111111111_opy_, bstack1lllll11l1ll_opy_ = self.bstack1llllll111l1_opy_()
      self.bstack1111ll1l111_opy_ = bstack1lllll11l1ll_opy_
      bstack111111111l1_opy_, bstack1lllll1ll1ll_opy_ = self.bstack1llllll1ll1l_opy_(bstack11111111111_opy_, bstack1lllll11l1ll_opy_)
      if bstack1lllll1ll1ll_opy_:
        self.binary_path = bstack111111111l1_opy_
        thread = Thread(target=self.bstack1lllll1l11ll_opy_)
        thread.start()
      else:
        self.bstack1lllll11ll11_opy_ = True
        self.logger.error(bstack1l111ll_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥ὿").format(bstack111111111l1_opy_))
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾀ").format(e))
  def bstack1lllll1l1ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l111ll_opy_ (u"ࠨ࡮ࡲ࡫ࠬᾁ"), bstack1l111ll_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬᾂ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢᾃ").format(logfile))
      self.bstack1llllll1llll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾄ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1l111l_opy_, stage=STAGE.bstack1ll11l111l_opy_)
  def bstack1lllll1l11ll_opy_(self):
    bstack11111111ll1_opy_ = self.bstack1llllll1111l_opy_()
    if bstack11111111ll1_opy_ == None:
      self.bstack1lllll11ll11_opy_ = True
      self.logger.error(bstack1l111ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣᾅ"))
      return False
    bstack1111111l1l1_opy_ = [bstack1l111ll_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢᾆ") if self.bstack1llll1l11l_opy_ else bstack1l111ll_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᾇ")]
    bstack11111l1ll11_opy_ = self.bstack1llllll1lll1_opy_()
    if bstack11111l1ll11_opy_ != None:
      bstack1111111l1l1_opy_.append(bstack1l111ll_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᾈ").format(bstack11111l1ll11_opy_))
    env = os.environ.copy()
    env[bstack1l111ll_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᾉ")] = bstack11111111ll1_opy_
    env[bstack1l111ll_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥᾊ")] = os.environ.get(bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᾋ"), bstack1l111ll_opy_ (u"ࠬ࠭ᾌ"))
    bstack11111111lll_opy_ = [self.binary_path]
    self.bstack1lllll1l1ll1_opy_()
    self.bstack1lllllll1ll1_opy_ = self.bstack1lllllllll11_opy_(bstack11111111lll_opy_ + bstack1111111l1l1_opy_, env)
    self.logger.debug(bstack1l111ll_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᾍ"))
    bstack1llllll11lll_opy_ = 0
    while self.bstack1lllllll1ll1_opy_.poll() == None:
      bstack1lllll1l1lll_opy_ = self.bstack11111111l1l_opy_()
      if bstack1lllll1l1lll_opy_:
        self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᾎ"))
        self.bstack1111111111l_opy_ = True
        return True
      bstack1llllll11lll_opy_ += 1
      self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᾏ").format(bstack1llllll11lll_opy_))
      time.sleep(2)
    self.logger.error(bstack1l111ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᾐ").format(bstack1llllll11lll_opy_))
    self.bstack1lllll11ll11_opy_ = True
    return False
  def bstack11111111l1l_opy_(self, bstack1llllll11lll_opy_ = 0):
    if bstack1llllll11lll_opy_ > 10:
      return False
    try:
      bstack1llllll11l11_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᾑ"), bstack1l111ll_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᾒ"))
      bstack1llllll111ll_opy_ = bstack1llllll11l11_opy_ + bstack11l11l1l11l_opy_
      response = requests.get(bstack1llllll111ll_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l111ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᾓ"), {}).get(bstack1l111ll_opy_ (u"࠭ࡩࡥࠩᾔ"), None)
      return True
    except:
      self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᾕ"))
      return False
  def bstack1llllll1111l_opy_(self):
    bstack1lllllll1l1l_opy_ = bstack1l111ll_opy_ (u"ࠨࡣࡳࡴࠬᾖ") if self.bstack1llll1l11l_opy_ else bstack1l111ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᾗ")
    bstack1lllll1l1111_opy_ = bstack1l111ll_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾘ") if self.config.get(bstack1l111ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾙ")) is None else True
    bstack11ll111ll11_opy_ = bstack1l111ll_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨᾚ").format(self.config[bstack1l111ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᾛ")], bstack1lllllll1l1l_opy_, bstack1lllll1l1111_opy_)
    if self.percy_capture_mode:
      bstack11ll111ll11_opy_ += bstack1l111ll_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤᾜ").format(self.percy_capture_mode)
    uri = bstack11llllll11_opy_(bstack11ll111ll11_opy_)
    try:
      response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠨࡉࡈࡘࠬᾝ"), uri, {}, {bstack1l111ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᾞ"): (self.config[bstack1l111ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᾟ")], self.config[bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᾠ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11ll1l1l_opy_ = data.get(bstack1l111ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ᾡ"))
        self.percy_capture_mode = data.get(bstack1l111ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫᾢ"))
        os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᾣ")] = str(self.bstack1l11ll1l1l_opy_)
        os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᾤ")] = str(self.percy_capture_mode)
        if bstack1lllll1l1111_opy_ == bstack1l111ll_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾥ") and str(self.bstack1l11ll1l1l_opy_).lower() == bstack1l111ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᾦ"):
          self.bstack1ll1l1l111_opy_ = True
        if bstack1l111ll_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾧ") in data:
          return data[bstack1l111ll_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾨ")]
        else:
          raise bstack1l111ll_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᾩ").format(data)
      else:
        raise bstack1l111ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᾪ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᾫ").format(e))
  def bstack1llllll1lll1_opy_(self):
    bstack1llllllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᾬ"))
    try:
      if bstack1l111ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾭ") not in self.bstack1lllll1llll1_opy_:
        self.bstack1lllll1llll1_opy_[bstack1l111ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾮ")] = 2
      with open(bstack1llllllllll1_opy_, bstack1l111ll_opy_ (u"ࠬࡽࠧᾯ")) as fp:
        json.dump(self.bstack1lllll1llll1_opy_, fp)
      return bstack1llllllllll1_opy_
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾰ").format(e))
  def bstack1lllllllll11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l1ll_opy_ == bstack1l111ll_opy_ (u"ࠧࡸ࡫ࡱࠫᾱ"):
        bstack1111111l1ll_opy_ = [bstack1l111ll_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᾲ"), bstack1l111ll_opy_ (u"ࠩ࠲ࡧࠬᾳ")]
        cmd = bstack1111111l1ll_opy_ + cmd
      cmd = bstack1l111ll_opy_ (u"ࠪࠤࠬᾴ").join(cmd)
      self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣ᾵").format(cmd))
      with open(self.bstack1llllll1llll_opy_, bstack1l111ll_opy_ (u"ࠧࡧࠢᾶ")) as bstack1lllll1l1l1l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll1l1l1l_opy_, text=True, stderr=bstack1lllll1l1l1l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll11ll11_opy_ = True
      self.logger.error(bstack1l111ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾷ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1111111111l_opy_:
        self.logger.info(bstack1l111ll_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᾸ"))
        cmd = [self.binary_path, bstack1l111ll_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᾹ")]
        self.bstack1lllllllll11_opy_(cmd)
        self.bstack1111111111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᾺ").format(cmd, e))
  def bstack1l1l111l1l_opy_(self):
    if not self.bstack1l11ll1l1l_opy_:
      return
    try:
      bstack1lllllll1l11_opy_ = 0
      while not self.bstack1111111111l_opy_ and bstack1lllllll1l11_opy_ < self.bstack1111111ll1l_opy_:
        if self.bstack1lllll11ll11_opy_:
          self.logger.info(bstack1l111ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣΆ"))
          return
        time.sleep(1)
        bstack1lllllll1l11_opy_ += 1
      os.environ[bstack1l111ll_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᾼ")] = str(self.bstack1lllllll1lll_opy_())
      self.logger.info(bstack1l111ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨ᾽"))
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢι").format(e))
  def bstack1lllllll1lll_opy_(self):
    if self.bstack1llll1l11l_opy_:
      return
    try:
      bstack1llllllll1l1_opy_ = [platform[bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ᾿")].lower() for platform in self.config.get(bstack1l111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῀"), [])]
      bstack1lllll1l1l11_opy_ = sys.maxsize
      bstack1llllllll11l_opy_ = bstack1l111ll_opy_ (u"ࠩࠪ῁")
      for browser in bstack1llllllll1l1_opy_:
        if browser in self.bstack11111111l11_opy_:
          bstack1lllll11lll1_opy_ = self.bstack11111111l11_opy_[browser]
        if bstack1lllll11lll1_opy_ < bstack1lllll1l1l11_opy_:
          bstack1lllll1l1l11_opy_ = bstack1lllll11lll1_opy_
          bstack1llllllll11l_opy_ = browser
      return bstack1llllllll11l_opy_
    except Exception as e:
      self.logger.error(bstack1l111ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦῂ").format(e))
  @classmethod
  def bstack1ll1l111l_opy_(self):
    return os.getenv(bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩῃ"), bstack1l111ll_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫῄ")).lower()
  @classmethod
  def bstack11l111ll1_opy_(self):
    return os.getenv(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪ῅"), bstack1l111ll_opy_ (u"ࠧࠨῆ"))
  @classmethod
  def bstack11llll1ll1l_opy_(cls, value):
    cls.bstack1ll1l1l111_opy_ = value
  @classmethod
  def bstack1llllll11ll1_opy_(cls):
    return cls.bstack1ll1l1l111_opy_
  @classmethod
  def bstack11lllll111l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll11111_opy_(cls):
    return cls.percy_build_id