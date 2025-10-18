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
from bstack_utils.helper import bstack111l1llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1l1ll1ll_opy_ import bstack11l1l11l1_opy_
class bstack1l11ll1ll1_opy_:
  working_dir = os.getcwd()
  bstack1l11l1111l_opy_ = False
  config = {}
  bstack1111l1l1l11_opy_ = bstack11l111_opy_ (u"ࠨࠩὉ")
  binary_path = bstack11l111_opy_ (u"ࠩࠪὊ")
  bstack1lllllll1111_opy_ = bstack11l111_opy_ (u"ࠪࠫὋ")
  bstack11l1llll1_opy_ = False
  bstack1111111lll1_opy_ = None
  bstack1lllll1lllll_opy_ = {}
  bstack1lllllllll1l_opy_ = 300
  bstack1llllll1l111_opy_ = False
  logger = None
  bstack1lllllll111l_opy_ = False
  bstack111l11lll1_opy_ = False
  percy_build_id = None
  bstack1lllllll11ll_opy_ = bstack11l111_opy_ (u"ࠫࠬὌ")
  bstack11111111lll_opy_ = {
    bstack11l111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬὍ") : 1,
    bstack11l111_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧ὎") : 2,
    bstack11l111_opy_ (u"ࠧࡦࡦࡪࡩࠬ὏") : 3,
    bstack11l111_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨὐ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllll1ll11l_opy_(self):
    bstack1llllll1l1ll_opy_ = bstack11l111_opy_ (u"ࠩࠪὑ")
    bstack1lllllll1l1l_opy_ = sys.platform
    bstack1llllll11lll_opy_ = bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩὒ")
    if re.match(bstack11l111_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦὓ"), bstack1lllllll1l1l_opy_) != None:
      bstack1llllll1l1ll_opy_ = bstack11l11ll111l_opy_ + bstack11l111_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨὔ")
      self.bstack1lllllll11ll_opy_ = bstack11l111_opy_ (u"࠭࡭ࡢࡥࠪὕ")
    elif re.match(bstack11l111_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧὖ"), bstack1lllllll1l1l_opy_) != None:
      bstack1llllll1l1ll_opy_ = bstack11l11ll111l_opy_ + bstack11l111_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤὗ")
      bstack1llllll11lll_opy_ = bstack11l111_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧ὘")
      self.bstack1lllllll11ll_opy_ = bstack11l111_opy_ (u"ࠪࡻ࡮ࡴࠧὙ")
    else:
      bstack1llllll1l1ll_opy_ = bstack11l11ll111l_opy_ + bstack11l111_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢ὚")
      self.bstack1lllllll11ll_opy_ = bstack11l111_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫὛ")
    return bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_
  def bstack1llllll111ll_opy_(self):
    try:
      bstack1llllll1l1l1_opy_ = [os.path.join(expanduser(bstack11l111_opy_ (u"ࠨࡾࠣ὜")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧὝ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll1l1l1_opy_:
        if(self.bstack1lllll1l1lll_opy_(path)):
          return path
      raise bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧ὞")
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦὟ").format(e))
  def bstack1lllll1l1lll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111111111ll_opy_(self, bstack1llllll1ll11_opy_):
    return os.path.join(bstack1llllll1ll11_opy_, self.bstack1111l1l1l11_opy_ + bstack11l111_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤὠ"))
  def bstack1111111ll1l_opy_(self, bstack1llllll1ll11_opy_, bstack1lllllll1l11_opy_):
    if not bstack1lllllll1l11_opy_: return
    try:
      bstack1llllll11l1l_opy_ = self.bstack111111111ll_opy_(bstack1llllll1ll11_opy_)
      with open(bstack1llllll11l1l_opy_, bstack11l111_opy_ (u"ࠦࡼࠨὡ")) as f:
        f.write(bstack1lllllll1l11_opy_)
        self.logger.debug(bstack11l111_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤὢ"))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὣ").format(e))
  def bstack1lllll1l11ll_opy_(self, bstack1llllll1ll11_opy_):
    try:
      bstack1llllll11l1l_opy_ = self.bstack111111111ll_opy_(bstack1llllll1ll11_opy_)
      if os.path.exists(bstack1llllll11l1l_opy_):
        with open(bstack1llllll11l1l_opy_, bstack11l111_opy_ (u"ࠢࡳࠤὤ")) as f:
          bstack1lllllll1l11_opy_ = f.read().strip()
          return bstack1lllllll1l11_opy_ if bstack1lllllll1l11_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦὥ").format(e))
  def bstack1lllll1ll111_opy_(self, bstack1llllll1ll11_opy_, bstack1llllll1l1ll_opy_):
    bstack1llllll111l1_opy_ = self.bstack1lllll1l11ll_opy_(bstack1llllll1ll11_opy_)
    if bstack1llllll111l1_opy_:
      try:
        bstack1llllll1ll1l_opy_ = self.bstack1lllllll1ll1_opy_(bstack1llllll111l1_opy_, bstack1llllll1l1ll_opy_)
        if not bstack1llllll1ll1l_opy_:
          self.logger.debug(bstack11l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦὦ"))
          return True
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤὧ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥὨ").format(e))
    return False
  def bstack1lllllll1ll1_opy_(self, bstack1llllll111l1_opy_, bstack1llllll1l1ll_opy_):
    try:
      headers = {
        bstack11l111_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧὩ"): bstack1llllll111l1_opy_
      }
      response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"࠭ࡇࡆࡖࠪὪ"), bstack1llllll1l1ll_opy_, {}, {bstack11l111_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣὫ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥὬ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1l1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
  def bstack1llllll1lll1_opy_(self, bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_):
    try:
      bstack1lllll1l111l_opy_ = self.bstack1llllll111ll_opy_()
      bstack1lllll1l11l1_opy_ = os.path.join(bstack1lllll1l111l_opy_, bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬὭ"))
      bstack1111111l1ll_opy_ = os.path.join(bstack1lllll1l111l_opy_, bstack1llllll11lll_opy_)
      if self.bstack1lllll1ll111_opy_(bstack1lllll1l111l_opy_, bstack1llllll1l1ll_opy_): # if bstack1lllll1llll1_opy_, bstack1llll1l11ll_opy_ bstack1lllllll1l11_opy_ is bstack1llllll11ll1_opy_ to bstack1111ll11ll1_opy_ version available (response 304)
        if os.path.exists(bstack1111111l1ll_opy_):
          self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧὮ").format(bstack1111111l1ll_opy_))
          return bstack1111111l1ll_opy_
        if os.path.exists(bstack1lllll1l11l1_opy_):
          self.logger.info(bstack11l111_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤὯ").format(bstack1lllll1l11l1_opy_))
          return self.bstack1111111l111_opy_(bstack1lllll1l11l1_opy_, bstack1llllll11lll_opy_)
      self.logger.info(bstack11l111_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥὰ").format(bstack1llllll1l1ll_opy_))
      response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"࠭ࡇࡆࡖࠪά"), bstack1llllll1l1ll_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll1lll1l_opy_ = response.headers.get(bstack11l111_opy_ (u"ࠢࡆࡖࡤ࡫ࠧὲ"), bstack11l111_opy_ (u"ࠣࠤέ"))
        if bstack1lllll1lll1l_opy_:
          self.bstack1111111ll1l_opy_(bstack1lllll1l111l_opy_, bstack1lllll1lll1l_opy_)
        with open(bstack1lllll1l11l1_opy_, bstack11l111_opy_ (u"ࠩࡺࡦࠬὴ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l111_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣή").format(bstack1lllll1l11l1_opy_))
        return self.bstack1111111l111_opy_(bstack1lllll1l11l1_opy_, bstack1llllll11lll_opy_)
      else:
        raise(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢὶ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨί").format(e))
  def bstack11111111l11_opy_(self, bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_):
    try:
      retry = 2
      bstack1111111l1ll_opy_ = None
      bstack1111111l11l_opy_ = False
      while retry > 0:
        bstack1111111l1ll_opy_ = self.bstack1llllll1lll1_opy_(bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_)
        bstack1111111l11l_opy_ = self.bstack1lllll1lll11_opy_(bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_, bstack1111111l1ll_opy_)
        if bstack1111111l11l_opy_:
          break
        retry -= 1
      return bstack1111111l1ll_opy_, bstack1111111l11l_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥὸ").format(e))
    return bstack1111111l1ll_opy_, False
  def bstack1lllll1lll11_opy_(self, bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_, bstack1111111l1ll_opy_, bstack1llllll1llll_opy_ = 0):
    if bstack1llllll1llll_opy_ > 1:
      return False
    if bstack1111111l1ll_opy_ == None or os.path.exists(bstack1111111l1ll_opy_) == False:
      self.logger.warn(bstack11l111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧό"))
      return False
    bstack1lllll11lll1_opy_ = bstack11l111_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤὺ")
    command = bstack11l111_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨύ").format(bstack1111111l1ll_opy_)
    bstack11111111ll1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll11lll1_opy_, bstack11111111ll1_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤὼ"))
      return False
  def bstack1111111l111_opy_(self, bstack1lllll1l11l1_opy_, bstack1llllll11lll_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l11l1_opy_)
      shutil.unpack_archive(bstack1lllll1l11l1_opy_, working_dir)
      bstack1111111l1ll_opy_ = os.path.join(working_dir, bstack1llllll11lll_opy_)
      os.chmod(bstack1111111l1ll_opy_, 0o755)
      return bstack1111111l1ll_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧώ"))
  def bstack1lllll1ll1ll_opy_(self):
    try:
      bstack1lllllllll11_opy_ = self.config.get(bstack11l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ὾"))
      bstack1lllll1ll1ll_opy_ = bstack1lllllllll11_opy_ or (bstack1lllllllll11_opy_ is None and self.bstack1l11l1111l_opy_)
      if not bstack1lllll1ll1ll_opy_ or self.config.get(bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ὿"), None) not in bstack11l1l1111l1_opy_:
        return False
      self.bstack11l1llll1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾀ").format(e))
  def bstack1llllllll1ll_opy_(self):
    try:
      bstack1llllllll1ll_opy_ = self.percy_capture_mode
      return bstack1llllllll1ll_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾁ").format(e))
  def init(self, bstack1l11l1111l_opy_, config, logger):
    self.bstack1l11l1111l_opy_ = bstack1l11l1111l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1ll1ll_opy_():
      return
    self.bstack1lllll1lllll_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᾂ"), {})
    self.percy_capture_mode = config.get(bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᾃ"))
    try:
      bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_ = self.bstack1lllll1ll11l_opy_()
      self.bstack1111l1l1l11_opy_ = bstack1llllll11lll_opy_
      bstack1111111l1ll_opy_, bstack1111111l11l_opy_ = self.bstack11111111l11_opy_(bstack1llllll1l1ll_opy_, bstack1llllll11lll_opy_)
      if bstack1111111l11l_opy_:
        self.binary_path = bstack1111111l1ll_opy_
        thread = Thread(target=self.bstack1lllllllllll_opy_)
        thread.start()
      else:
        self.bstack1lllllll111l_opy_ = True
        self.logger.error(bstack11l111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣᾄ").format(bstack1111111l1ll_opy_))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾅ").format(e))
  def bstack11111111111_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l111_opy_ (u"࠭࡬ࡰࡩࠪᾆ"), bstack11l111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪᾇ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l111_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧᾈ").format(logfile))
      self.bstack1lllllll1111_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾉ").format(e))
  @measure(event_name=EVENTS.bstack11l11l1ll1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
  def bstack1lllllllllll_opy_(self):
    bstack1111111l1l1_opy_ = self.bstack1lllll1ll1l1_opy_()
    if bstack1111111l1l1_opy_ == None:
      self.bstack1lllllll111l_opy_ = True
      self.logger.error(bstack11l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨᾊ"))
      return False
    bstack1llllll11111_opy_ = [bstack11l111_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧᾋ") if self.bstack1l11l1111l_opy_ else bstack11l111_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩᾌ")]
    bstack11111ll1l11_opy_ = self.bstack1llllll1l11l_opy_()
    if bstack11111ll1l11_opy_ != None:
      bstack1llllll11111_opy_.append(bstack11l111_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧᾍ").format(bstack11111ll1l11_opy_))
    env = os.environ.copy()
    env[bstack11l111_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧᾎ")] = bstack1111111l1l1_opy_
    env[bstack11l111_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣᾏ")] = os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᾐ"), bstack11l111_opy_ (u"ࠪࠫᾑ"))
    bstack1llllll11l11_opy_ = [self.binary_path]
    self.bstack11111111111_opy_()
    self.bstack1111111lll1_opy_ = self.bstack1llllllll11l_opy_(bstack1llllll11l11_opy_ + bstack1llllll11111_opy_, env)
    self.logger.debug(bstack11l111_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧᾒ"))
    bstack1llllll1llll_opy_ = 0
    while self.bstack1111111lll1_opy_.poll() == None:
      bstack1llllllllll1_opy_ = self.bstack1lllll1l1111_opy_()
      if bstack1llllllllll1_opy_:
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣᾓ"))
        self.bstack1llllll1l111_opy_ = True
        return True
      bstack1llllll1llll_opy_ += 1
      self.logger.debug(bstack11l111_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤᾔ").format(bstack1llllll1llll_opy_))
      time.sleep(2)
    self.logger.error(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧᾕ").format(bstack1llllll1llll_opy_))
    self.bstack1lllllll111l_opy_ = True
    return False
  def bstack1lllll1l1111_opy_(self, bstack1llllll1llll_opy_ = 0):
    if bstack1llllll1llll_opy_ > 10:
      return False
    try:
      bstack1111111ll11_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨᾖ"), bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪᾗ"))
      bstack111111111l1_opy_ = bstack1111111ll11_opy_ + bstack11l11ll1111_opy_
      response = requests.get(bstack111111111l1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩᾘ"), {}).get(bstack11l111_opy_ (u"ࠫ࡮ࡪࠧᾙ"), None)
      return True
    except:
      self.logger.debug(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥᾚ"))
      return False
  def bstack1lllll1ll1l1_opy_(self):
    bstack1llllllll111_opy_ = bstack11l111_opy_ (u"࠭ࡡࡱࡲࠪᾛ") if self.bstack1l11l1111l_opy_ else bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᾜ")
    bstack1llllllll1l1_opy_ = bstack11l111_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᾝ") if self.config.get(bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᾞ")) is None else True
    bstack11ll111ll11_opy_ = bstack11l111_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦᾟ").format(self.config[bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᾠ")], bstack1llllllll111_opy_, bstack1llllllll1l1_opy_)
    if self.percy_capture_mode:
      bstack11ll111ll11_opy_ += bstack11l111_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢᾡ").format(self.percy_capture_mode)
    uri = bstack11l1l11l1_opy_(bstack11ll111ll11_opy_)
    try:
      response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"࠭ࡇࡆࡖࠪᾢ"), uri, {}, {bstack11l111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᾣ"): (self.config[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᾤ")], self.config[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᾥ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l1llll1_opy_ = data.get(bstack11l111_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫᾦ"))
        self.percy_capture_mode = data.get(bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩᾧ"))
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᾨ")] = str(self.bstack11l1llll1_opy_)
        os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᾩ")] = str(self.percy_capture_mode)
        if bstack1llllllll1l1_opy_ == bstack11l111_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥᾪ") and str(self.bstack11l1llll1_opy_).lower() == bstack11l111_opy_ (u"ࠣࡶࡵࡹࡪࠨᾫ"):
          self.bstack111l11lll1_opy_ = True
        if bstack11l111_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣᾬ") in data:
          return data[bstack11l111_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾭ")]
        else:
          raise bstack11l111_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫᾮ").format(data)
      else:
        raise bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧᾯ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢᾰ").format(e))
  def bstack1llllll1l11l_opy_(self):
    bstack1lllll11ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥᾱ"))
    try:
      if bstack11l111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᾲ") not in self.bstack1lllll1lllll_opy_:
        self.bstack1lllll1lllll_opy_[bstack11l111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾳ")] = 2
      with open(bstack1lllll11ll1l_opy_, bstack11l111_opy_ (u"ࠪࡻࠬᾴ")) as fp:
        json.dump(self.bstack1lllll1lllll_opy_, fp)
      return bstack1lllll11ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ᾵").format(e))
  def bstack1llllllll11l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllllll11ll_opy_ == bstack11l111_opy_ (u"ࠬࡽࡩ࡯ࠩᾶ"):
        bstack1111111llll_opy_ = [bstack11l111_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧᾷ"), bstack11l111_opy_ (u"ࠧ࠰ࡥࠪᾸ")]
        cmd = bstack1111111llll_opy_ + cmd
      cmd = bstack11l111_opy_ (u"ࠨࠢࠪᾹ").join(cmd)
      self.logger.debug(bstack11l111_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨᾺ").format(cmd))
      with open(self.bstack1lllllll1111_opy_, bstack11l111_opy_ (u"ࠥࡥࠧΆ")) as bstack1lllll1l1ll1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll1l1ll1_opy_, text=True, stderr=bstack1lllll1l1ll1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllllll111l_opy_ = True
      self.logger.error(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᾼ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1l111_opy_:
        self.logger.info(bstack11l111_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨ᾽"))
        cmd = [self.binary_path, bstack11l111_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤι")]
        self.bstack1llllllll11l_opy_(cmd)
        self.bstack1llllll1l111_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢ᾿").format(cmd, e))
  def bstack1111l11lll_opy_(self):
    if not self.bstack11l1llll1_opy_:
      return
    try:
      bstack1lllll1l1l11_opy_ = 0
      while not self.bstack1llllll1l111_opy_ and bstack1lllll1l1l11_opy_ < self.bstack1lllllllll1l_opy_:
        if self.bstack1lllllll111l_opy_:
          self.logger.info(bstack11l111_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨ῀"))
          return
        time.sleep(1)
        bstack1lllll1l1l11_opy_ += 1
      os.environ[bstack11l111_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨ῁")] = str(self.bstack1lllll1l1l1l_opy_())
      self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦῂ"))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧῃ").format(e))
  def bstack1lllll1l1l1l_opy_(self):
    if self.bstack1l11l1111l_opy_:
      return
    try:
      bstack1lllll11llll_opy_ = [platform[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪῄ")].lower() for platform in self.config.get(bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ῅"), [])]
      bstack1lllllll1lll_opy_ = sys.maxsize
      bstack1lllllll11l1_opy_ = bstack11l111_opy_ (u"ࠧࠨῆ")
      for browser in bstack1lllll11llll_opy_:
        if browser in self.bstack11111111lll_opy_:
          bstack11111111l1l_opy_ = self.bstack11111111lll_opy_[browser]
        if bstack11111111l1l_opy_ < bstack1lllllll1lll_opy_:
          bstack1lllllll1lll_opy_ = bstack11111111l1l_opy_
          bstack1lllllll11l1_opy_ = browser
      return bstack1lllllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤῇ").format(e))
  @classmethod
  def bstack1l1lllll1l_opy_(self):
    return os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧῈ"), bstack11l111_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩΈ")).lower()
  @classmethod
  def bstack1l1l1l111l_opy_(self):
    return os.getenv(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨῊ"), bstack11l111_opy_ (u"ࠬ࠭Ή"))
  @classmethod
  def bstack11lllll111l_opy_(cls, value):
    cls.bstack111l11lll1_opy_ = value
  @classmethod
  def bstack1111111111l_opy_(cls):
    return cls.bstack111l11lll1_opy_
  @classmethod
  def bstack11lllll11ll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1111l_opy_(cls):
    return cls.percy_build_id