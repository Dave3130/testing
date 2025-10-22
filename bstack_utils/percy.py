# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
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
from bstack_utils.helper import bstack11l1l111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l11l1l111_opy_ import bstack1l111ll1l1_opy_
class bstack11111lll1l_opy_:
  working_dir = os.getcwd()
  bstack1l1l111l11_opy_ = False
  config = {}
  bstack1111l1l1l11_opy_ = bstack1lllll1l_opy_ (u"࠭ࠧ὇")
  binary_path = bstack1lllll1l_opy_ (u"ࠧࠨὈ")
  bstack1llllll111ll_opy_ = bstack1lllll1l_opy_ (u"ࠨࠩὉ")
  bstack1l11lll1ll_opy_ = False
  bstack1111111l1l1_opy_ = None
  bstack11111111l11_opy_ = {}
  bstack1lllll1ll1ll_opy_ = 300
  bstack1llllll1l1ll_opy_ = False
  logger = None
  bstack1llllll1l1l1_opy_ = False
  bstack1ll1l1ll1l_opy_ = False
  percy_build_id = None
  bstack1lllll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪὊ")
  bstack1llllll1ll1l_opy_ = {
    bstack1lllll1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪὋ") : 1,
    bstack1lllll1l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬὌ") : 2,
    bstack1lllll1l_opy_ (u"ࠬ࡫ࡤࡨࡧࠪὍ") : 3,
    bstack1lllll1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭὎") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111111l1ll_opy_(self):
    bstack1llllll111l1_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨ὏")
    bstack1llllll1l11l_opy_ = sys.platform
    bstack1llllllllll1_opy_ = bstack1lllll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧὐ")
    if re.match(bstack1lllll1l_opy_ (u"ࠤࡧࡥࡷࡽࡩ࡯ࡾࡰࡥࡨࠦ࡯ࡴࠤὑ"), bstack1llllll1l11l_opy_) != None:
      bstack1llllll111l1_opy_ = bstack11l11ll1111_opy_ + bstack1lllll1l_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡳࡸࡾ࠮ࡻ࡫ࡳࠦὒ")
      self.bstack1lllll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠫࡲࡧࡣࠨὓ")
    elif re.match(bstack1lllll1l_opy_ (u"ࠧࡳࡳࡸ࡫ࡱࢀࡲࡹࡹࡴࡾࡰ࡭ࡳ࡭ࡷࡽࡥࡼ࡫ࡼ࡯࡮ࡽࡤࡦࡧࡼ࡯࡮ࡽࡹ࡬ࡲࡨ࡫ࡼࡦ࡯ࡦࢀࡼ࡯࡮࠴࠴ࠥὔ"), bstack1llllll1l11l_opy_) != None:
      bstack1llllll111l1_opy_ = bstack11l11ll1111_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳ࡷࡪࡰ࠱ࡾ࡮ࡶࠢὕ")
      bstack1llllllllll1_opy_ = bstack1lllll1l_opy_ (u"ࠢࡱࡧࡵࡧࡾ࠴ࡥࡹࡧࠥὖ")
      self.bstack1lllll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠨࡹ࡬ࡲࠬὗ")
    else:
      bstack1llllll111l1_opy_ = bstack11l11ll1111_opy_ + bstack1lllll1l_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯࡯࡭ࡳࡻࡸ࠯ࡼ࡬ࡴࠧ὘")
      self.bstack1lllll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩὙ")
    return bstack1llllll111l1_opy_, bstack1llllllllll1_opy_
  def bstack1llllllll111_opy_(self):
    try:
      bstack111111111l1_opy_ = [os.path.join(expanduser(bstack1lllll1l_opy_ (u"ࠦࢃࠨ὚")), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬὛ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111111111l1_opy_:
        if(self.bstack1lllllllll1l_opy_(path)):
          return path
      raise bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥ὜")
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠲ࠦࡻࡾࠤὝ").format(e))
  def bstack1lllllllll1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllllll1ll_opy_(self, bstack1llllll11111_opy_):
    return os.path.join(bstack1llllll11111_opy_, self.bstack1111l1l1l11_opy_ + bstack1lllll1l_opy_ (u"ࠣ࠰ࡨࡸࡦ࡭ࠢ὞"))
  def bstack1lllll1ll111_opy_(self, bstack1llllll11111_opy_, bstack1lllllll11ll_opy_):
    if not bstack1lllllll11ll_opy_: return
    try:
      bstack11111111lll_opy_ = self.bstack1llllllll1ll_opy_(bstack1llllll11111_opy_)
      with open(bstack11111111lll_opy_, bstack1lllll1l_opy_ (u"ࠤࡺࠦὟ")) as f:
        f.write(bstack1lllllll11ll_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡗࡦࡼࡥࡥࠢࡱࡩࡼࠦࡅࡕࡣࡪࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠢὠ"))
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥࡺࡨࡦࠢࡨࡸࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦὡ").format(e))
  def bstack1lllll1l11ll_opy_(self, bstack1llllll11111_opy_):
    try:
      bstack11111111lll_opy_ = self.bstack1llllllll1ll_opy_(bstack1llllll11111_opy_)
      if os.path.exists(bstack11111111lll_opy_):
        with open(bstack11111111lll_opy_, bstack1lllll1l_opy_ (u"ࠧࡸࠢὢ")) as f:
          bstack1lllllll11ll_opy_ = f.read().strip()
          return bstack1lllllll11ll_opy_ if bstack1lllllll11ll_opy_ else None
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡆࡖࡤ࡫࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤὣ").format(e))
  def bstack1111111lll1_opy_(self, bstack1llllll11111_opy_, bstack1llllll111l1_opy_):
    bstack1lllll1lllll_opy_ = self.bstack1lllll1l11ll_opy_(bstack1llllll11111_opy_)
    if bstack1lllll1lllll_opy_:
      try:
        bstack1llllll1l111_opy_ = self.bstack1lllllll1l11_opy_(bstack1lllll1lllll_opy_, bstack1llllll111l1_opy_)
        if not bstack1llllll1l111_opy_:
          self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡩࡴࠢࡸࡴࠥࡺ࡯ࠡࡦࡤࡸࡪࠦࠨࡆࡖࡤ࡫ࠥࡻ࡮ࡤࡪࡤࡲ࡬࡫ࡤࠪࠤὤ"))
          return True
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡐࡨࡻࠥࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡶࡲࡧࡥࡹ࡫ࠢὥ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1lllll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡵࡲࠡࡤ࡬ࡲࡦࡸࡹࠡࡷࡳࡨࡦࡺࡥࡴ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣὦ").format(e))
    return False
  def bstack1lllllll1l11_opy_(self, bstack1lllll1lllll_opy_, bstack1llllll111l1_opy_):
    try:
      headers = {
        bstack1lllll1l_opy_ (u"ࠥࡍ࡫࠳ࡎࡰࡰࡨ࠱ࡒࡧࡴࡤࡪࠥὧ"): bstack1lllll1lllll_opy_
      }
      response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠫࡌࡋࡔࠨὨ"), bstack1llllll111l1_opy_, {}, {bstack1lllll1l_opy_ (u"ࠧ࡮ࡥࡢࡦࡨࡶࡸࠨὩ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1lllll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠾ࠥࢁࡽࠣὪ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1111ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
  def bstack1lllllll1lll_opy_(self, bstack1llllll111l1_opy_, bstack1llllllllll1_opy_):
    try:
      bstack1lllllllll11_opy_ = self.bstack1llllllll111_opy_()
      bstack1lllllll111l_opy_ = os.path.join(bstack1lllllllll11_opy_, bstack1lllll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴ࡺࡪࡲࠪὫ"))
      bstack11111111111_opy_ = os.path.join(bstack1lllllllll11_opy_, bstack1llllllllll1_opy_)
      if self.bstack1111111lll1_opy_(bstack1lllllllll11_opy_, bstack1llllll111l1_opy_): # if bstack1lllllll1l1l_opy_, bstack1llll11l11l_opy_ bstack1lllllll11ll_opy_ is bstack1111111l11l_opy_ to bstack1111llll1ll_opy_ version available (response 304)
        if os.path.exists(bstack11111111111_opy_):
          self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡳ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥὬ").format(bstack11111111111_opy_))
          return bstack11111111111_opy_
        if os.path.exists(bstack1lllllll111l_opy_):
          self.logger.info(bstack1lllll1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡼ࡬ࡴࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡺࡴࡺࡪࡲࡳ࡭ࡳ࡭ࠢὭ").format(bstack1lllllll111l_opy_))
          return self.bstack1lllll1l1111_opy_(bstack1lllllll111l_opy_, bstack1llllllllll1_opy_)
      self.logger.info(bstack1lllll1l_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱࠥࢁࡽࠣὮ").format(bstack1llllll111l1_opy_))
      response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠫࡌࡋࡔࠨὯ"), bstack1llllll111l1_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllllll1111_opy_ = response.headers.get(bstack1lllll1l_opy_ (u"ࠧࡋࡔࡢࡩࠥὰ"), bstack1lllll1l_opy_ (u"ࠨࠢά"))
        if bstack1lllllll1111_opy_:
          self.bstack1lllll1ll111_opy_(bstack1lllllllll11_opy_, bstack1lllllll1111_opy_)
        with open(bstack1lllllll111l_opy_, bstack1lllll1l_opy_ (u"ࠧࡸࡤࠪὲ")) as file:
          file.write(response.content)
        self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࢂࠨέ").format(bstack1lllllll111l_opy_))
        return self.bstack1lllll1l1111_opy_(bstack1lllllll111l_opy_, bstack1llllllllll1_opy_)
      else:
        raise(bstack1lllll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࢁࠧὴ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦή").format(e))
  def bstack1llllll1lll1_opy_(self, bstack1llllll111l1_opy_, bstack1llllllllll1_opy_):
    try:
      retry = 2
      bstack11111111111_opy_ = None
      bstack1llllllll11l_opy_ = False
      while retry > 0:
        bstack11111111111_opy_ = self.bstack1lllllll1lll_opy_(bstack1llllll111l1_opy_, bstack1llllllllll1_opy_)
        bstack1llllllll11l_opy_ = self.bstack1lllll1ll1l1_opy_(bstack1llllll111l1_opy_, bstack1llllllllll1_opy_, bstack11111111111_opy_)
        if bstack1llllllll11l_opy_:
          break
        retry -= 1
      return bstack11111111111_opy_, bstack1llllllll11l_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣὶ").format(e))
    return bstack11111111111_opy_, False
  def bstack1lllll1ll1l1_opy_(self, bstack1llllll111l1_opy_, bstack1llllllllll1_opy_, bstack11111111111_opy_, bstack1111111111l_opy_ = 0):
    if bstack1111111111l_opy_ > 1:
      return False
    if bstack11111111111_opy_ == None or os.path.exists(bstack11111111111_opy_) == False:
      self.logger.warn(bstack1lllll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥί"))
      return False
    bstack111111111ll_opy_ = bstack1lllll1l_opy_ (u"ࡸࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࠲ࡧࡱ࡯ࠠ࡝ࡦ࠮ࡠ࠳ࡢࡤࠬ࡞࠱ࡠࡩ࠱ࠢὸ")
    command = bstack1lllll1l_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ό").format(bstack11111111111_opy_)
    bstack1llllllll1l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111111111ll_opy_, bstack1llllllll1l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢὺ"))
      return False
  def bstack1lllll1l1111_opy_(self, bstack1lllllll111l_opy_, bstack1llllllllll1_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllll111l_opy_)
      shutil.unpack_archive(bstack1lllllll111l_opy_, working_dir)
      bstack11111111111_opy_ = os.path.join(working_dir, bstack1llllllllll1_opy_)
      os.chmod(bstack11111111111_opy_, 0o755)
      return bstack11111111111_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥύ"))
  def bstack1lllll1l111l_opy_(self):
    try:
      bstack1lllll1l1l1l_opy_ = self.config.get(bstack1lllll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩὼ"))
      bstack1lllll1l111l_opy_ = bstack1lllll1l1l1l_opy_ or (bstack1lllll1l1l1l_opy_ is None and self.bstack1l1l111l11_opy_)
      if not bstack1lllll1l111l_opy_ or self.config.get(bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧώ"), None) not in bstack11l11lll1l1_opy_:
        return False
      self.bstack1l11lll1ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὾").format(e))
  def bstack11111111ll1_opy_(self):
    try:
      bstack11111111ll1_opy_ = self.percy_capture_mode
      return bstack11111111ll1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹࠡࡥࡤࡴࡹࡻࡲࡦࠢࡰࡳࡩ࡫ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὿").format(e))
  def init(self, bstack1l1l111l11_opy_, config, logger):
    self.bstack1l1l111l11_opy_ = bstack1l1l111l11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1l111l_opy_():
      return
    self.bstack11111111l11_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᾀ"), {})
    self.percy_capture_mode = config.get(bstack1lllll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᾁ"))
    try:
      bstack1llllll111l1_opy_, bstack1llllllllll1_opy_ = self.bstack1111111l1ll_opy_()
      self.bstack1111l1l1l11_opy_ = bstack1llllllllll1_opy_
      bstack11111111111_opy_, bstack1llllllll11l_opy_ = self.bstack1llllll1lll1_opy_(bstack1llllll111l1_opy_, bstack1llllllllll1_opy_)
      if bstack1llllllll11l_opy_:
        self.binary_path = bstack11111111111_opy_
        thread = Thread(target=self.bstack1lllll1llll1_opy_)
        thread.start()
      else:
        self.bstack1llllll1l1l1_opy_ = True
        self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡴࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࠦ࠭ࠡࡽࢀ࠰࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡑࡧࡵࡧࡾࠨᾂ").format(bstack11111111111_opy_))
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾃ").format(e))
  def bstack1llllll1ll11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1lllll1l_opy_ (u"ࠫࡱࡵࡧࠨᾄ"), bstack1lllll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡱࡵࡧࠨᾅ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡐࡶࡵ࡫࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࡶࠤࡦࡺࠠࡼࡿࠥᾆ").format(logfile))
      self.bstack1llllll111ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࠣࡴࡦࡺࡨ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾇ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l1ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
  def bstack1lllll1llll1_opy_(self):
    bstack1lllll11llll_opy_ = self.bstack1lllll1l1ll1_opy_()
    if bstack1lllll11llll_opy_ == None:
      self.bstack1llllll1l1l1_opy_ = True
      self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠦᾈ"))
      return False
    bstack1llllll11ll1_opy_ = [bstack1lllll1l_opy_ (u"ࠤࡤࡴࡵࡀࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠥᾉ") if self.bstack1l1l111l11_opy_ else bstack1lllll1l_opy_ (u"ࠪࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠧᾊ")]
    bstack11111l1ll1l_opy_ = self.bstack1lllll11lll1_opy_()
    if bstack11111l1ll1l_opy_ != None:
      bstack1llllll11ll1_opy_.append(bstack1lllll1l_opy_ (u"ࠦ࠲ࡩࠠࡼࡿࠥᾋ").format(bstack11111l1ll1l_opy_))
    env = os.environ.copy()
    env[bstack1lllll1l_opy_ (u"ࠧࡖࡅࡓࡅ࡜ࡣ࡙ࡕࡋࡆࡐࠥᾌ")] = bstack1lllll11llll_opy_
    env[bstack1lllll1l_opy_ (u"ࠨࡔࡉࡡࡅ࡙ࡎࡒࡄࡠࡗࡘࡍࡉࠨᾍ")] = os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᾎ"), bstack1lllll1l_opy_ (u"ࠨࠩᾏ"))
    bstack1111111ll1l_opy_ = [self.binary_path]
    self.bstack1llllll1ll11_opy_()
    self.bstack1111111l1l1_opy_ = self.bstack1llllll11lll_opy_(bstack1111111ll1l_opy_ + bstack1llllll11ll1_opy_, env)
    self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡖࡸࡦࡸࡴࡪࡰࡪࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠥᾐ"))
    bstack1111111111l_opy_ = 0
    while self.bstack1111111l1l1_opy_.poll() == None:
      bstack1llllll1111l_opy_ = self.bstack1lllll1ll11l_opy_()
      if bstack1llllll1111l_opy_:
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࠨᾑ"))
        self.bstack1llllll1l1ll_opy_ = True
        return True
      bstack1111111111l_opy_ += 1
      self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡖࡪࡺࡲࡺࠢ࠰ࠤࢀࢃࠢᾒ").format(bstack1111111111l_opy_))
      time.sleep(2)
    self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡆࡢ࡫࡯ࡩࡩࠦࡡࡧࡶࡨࡶࠥࢁࡽࠡࡣࡷࡸࡪࡳࡰࡵࡵࠥᾓ").format(bstack1111111111l_opy_))
    self.bstack1llllll1l1l1_opy_ = True
    return False
  def bstack1lllll1ll11l_opy_(self, bstack1111111111l_opy_ = 0):
    if bstack1111111111l_opy_ > 10:
      return False
    try:
      bstack11111111l1l_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤ࡙ࡅࡓࡘࡈࡖࡤࡇࡄࡅࡔࡈࡗࡘ࠭ᾔ"), bstack1lllll1l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶ࠽࠹࠸࠹࠸ࠨᾕ"))
      bstack1lllllll11l1_opy_ = bstack11111111l1l_opy_ + bstack11l1l1l111l_opy_
      response = requests.get(bstack1lllllll11l1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧᾖ"), {}).get(bstack1lllll1l_opy_ (u"ࠩ࡬ࡨࠬᾗ"), None)
      return True
    except:
      self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡰࡹ࡮ࠠࡤࡪࡨࡧࡰࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣᾘ"))
      return False
  def bstack1lllll1l1ll1_opy_(self):
    bstack1lllllll1ll1_opy_ = bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࠨᾙ") if self.bstack1l1l111l11_opy_ else bstack1lllll1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᾚ")
    bstack1lllll1l1lll_opy_ = bstack1lllll1l_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤᾛ") if self.config.get(bstack1lllll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᾜ")) is None else True
    bstack11ll11l1111_opy_ = bstack1lllll1l_opy_ (u"ࠣࡣࡳ࡭࠴ࡧࡰࡱࡡࡳࡩࡷࡩࡹ࠰ࡩࡨࡸࡤࡶࡲࡰ࡬ࡨࡧࡹࡥࡴࡰ࡭ࡨࡲࡄࡴࡡ࡮ࡧࡀࡿࢂࠬࡴࡺࡲࡨࡁࢀࢃࠦࡱࡧࡵࡧࡾࡃࡻࡾࠤᾝ").format(self.config[bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᾞ")], bstack1lllllll1ll1_opy_, bstack1lllll1l1lll_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1111_opy_ += bstack1lllll1l_opy_ (u"ࠥࠪࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦ࠿ࡾࢁࠧᾟ").format(self.percy_capture_mode)
    uri = bstack1l111ll1l1_opy_(bstack11ll11l1111_opy_)
    try:
      response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠫࡌࡋࡔࠨᾠ"), uri, {}, {bstack1lllll1l_opy_ (u"ࠬࡧࡵࡵࡪࠪᾡ"): (self.config[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᾢ")], self.config[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᾣ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11lll1ll_opy_ = data.get(bstack1lllll1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᾤ"))
        self.percy_capture_mode = data.get(bstack1lllll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡠࡥࡤࡴࡹࡻࡲࡦࡡࡰࡳࡩ࡫ࠧᾥ"))
        os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᾦ")] = str(self.bstack1l11lll1ll_opy_)
        os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᾧ")] = str(self.percy_capture_mode)
        if bstack1lllll1l1lll_opy_ == bstack1lllll1l_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣᾨ") and str(self.bstack1l11lll1ll_opy_).lower() == bstack1lllll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᾩ"):
          self.bstack1ll1l1ll1l_opy_ = True
        if bstack1lllll1l_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᾪ") in data:
          return data[bstack1lllll1l_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢᾫ")]
        else:
          raise bstack1lllll1l_opy_ (u"ࠩࡗࡳࡰ࡫࡮ࠡࡐࡲࡸࠥࡌ࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾࠩᾬ").format(data)
      else:
        raise bstack1lllll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡶࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡳࡵࡣࡷࡹࡸࠦ࠭ࠡࡽࢀ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡃࡱࡧࡽࠥ࠳ࠠࡼࡿࠥᾭ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡵࡸ࡯࡫ࡧࡦࡸࠧᾮ").format(e))
  def bstack1lllll11lll1_opy_(self):
    bstack1llllll11l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠧࡶࡥࡳࡥࡼࡇࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠣᾯ"))
    try:
      if bstack1lllll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᾰ") not in self.bstack11111111l11_opy_:
        self.bstack11111111l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨᾱ")] = 2
      with open(bstack1llllll11l1l_opy_, bstack1lllll1l_opy_ (u"ࠨࡹࠪᾲ")) as fp:
        json.dump(self.bstack11111111l11_opy_, fp)
      return bstack1llllll11l1l_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡩࡲࡦࡣࡷࡩࠥࡶࡥࡳࡥࡼࠤࡨࡵ࡮ࡧ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾳ").format(e))
  def bstack1llllll11lll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll1l1l11_opy_ == bstack1lllll1l_opy_ (u"ࠪࡻ࡮ࡴࠧᾴ"):
        bstack1111111l111_opy_ = [bstack1lllll1l_opy_ (u"ࠫࡨࡳࡤ࠯ࡧࡻࡩࠬ᾵"), bstack1lllll1l_opy_ (u"ࠬ࠵ࡣࠨᾶ")]
        cmd = bstack1111111l111_opy_ + cmd
      cmd = bstack1lllll1l_opy_ (u"࠭ࠠࠨᾷ").join(cmd)
      self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡓࡷࡱࡲ࡮ࡴࡧࠡࡽࢀࠦᾸ").format(cmd))
      with open(self.bstack1llllll111ll_opy_, bstack1lllll1l_opy_ (u"ࠣࡣࠥᾹ")) as bstack1lllll11ll1l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll11ll1l_opy_, text=True, stderr=bstack1lllll11ll1l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll1l1l1_opy_ = True
      self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠣࡻ࡮ࡺࡨࠡࡥࡰࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᾺ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1l1ll_opy_:
        self.logger.info(bstack1lllll1l_opy_ (u"ࠥࡗࡹࡵࡰࡱ࡫ࡱ࡫ࠥࡖࡥࡳࡥࡼࠦΆ"))
        cmd = [self.binary_path, bstack1lllll1l_opy_ (u"ࠦࡪࡾࡥࡤ࠼ࡶࡸࡴࡶࠢᾼ")]
        self.bstack1llllll11lll_opy_(cmd)
        self.bstack1llllll1l1ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡳࡵࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡩ࡯࡮࡯ࡤࡲࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ᾽").format(cmd, e))
  def bstack1111llll11_opy_(self):
    if not self.bstack1l11lll1ll_opy_:
      return
    try:
      bstack1lllll1lll11_opy_ = 0
      while not self.bstack1llllll1l1ll_opy_ and bstack1lllll1lll11_opy_ < self.bstack1lllll1ll1ll_opy_:
        if self.bstack1llllll1l1l1_opy_:
          self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤ࡫ࡧࡩ࡭ࡧࡧࠦι"))
          return
        time.sleep(1)
        bstack1lllll1lll11_opy_ += 1
      os.environ[bstack1lllll1l_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡂࡆࡕࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒ࠭᾿")] = str(self.bstack1llllll11l11_opy_())
      self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠤ῀"))
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ῁").format(e))
  def bstack1llllll11l11_opy_(self):
    if self.bstack1l1l111l11_opy_:
      return
    try:
      bstack1111111llll_opy_ = [platform[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨῂ")].lower() for platform in self.config.get(bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῃ"), [])]
      bstack1lllll1l11l1_opy_ = sys.maxsize
      bstack1111111ll11_opy_ = bstack1lllll1l_opy_ (u"ࠬ࠭ῄ")
      for browser in bstack1111111llll_opy_:
        if browser in self.bstack1llllll1ll1l_opy_:
          bstack1lllllllllll_opy_ = self.bstack1llllll1ll1l_opy_[browser]
        if bstack1lllllllllll_opy_ < bstack1lllll1l11l1_opy_:
          bstack1lllll1l11l1_opy_ = bstack1lllllllllll_opy_
          bstack1111111ll11_opy_ = browser
      return bstack1111111ll11_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡣࡧࡶࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ῅").format(e))
  @classmethod
  def bstack1lllll11l1_opy_(self):
    return os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬῆ"), bstack1lllll1l_opy_ (u"ࠨࡈࡤࡰࡸ࡫ࠧῇ")).lower()
  @classmethod
  def bstack1ll11l111_opy_(self):
    return os.getenv(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭Ὲ"), bstack1lllll1l_opy_ (u"ࠪࠫΈ"))
  @classmethod
  def bstack11lllll1111_opy_(cls, value):
    cls.bstack1ll1l1ll1l_opy_ = value
  @classmethod
  def bstack1lllll1lll1l_opy_(cls):
    return cls.bstack1ll1l1ll1l_opy_
  @classmethod
  def bstack11lllll1l1l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1llll_opy_(cls):
    return cls.percy_build_id