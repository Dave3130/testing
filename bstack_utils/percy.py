# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
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
from bstack_utils.helper import bstack11lll11l11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l1ll11ll_opy_ import bstack1l11l1111_opy_
class bstack111l1lll1l_opy_:
  working_dir = os.getcwd()
  bstack11llll1111_opy_ = False
  config = {}
  bstack1111lllll11_opy_ = bstack11l1l11_opy_ (u"ࠩࠪὃ")
  binary_path = bstack11l1l11_opy_ (u"ࠪࠫὄ")
  bstack1lllll1lll11_opy_ = bstack11l1l11_opy_ (u"ࠫࠬὅ")
  bstack1l1l1ll11_opy_ = False
  bstack1111111111l_opy_ = None
  bstack1llllll111ll_opy_ = {}
  bstack1llllll11111_opy_ = 300
  bstack1llllllll1ll_opy_ = False
  logger = None
  bstack1llllllllll1_opy_ = False
  bstack1111l1lll_opy_ = False
  percy_build_id = None
  bstack1llllll11l1l_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭὆")
  bstack1llllll11ll1_opy_ = {
    bstack11l1l11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭὇") : 1,
    bstack11l1l11_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨὈ") : 2,
    bstack11l1l11_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭Ὁ") : 3,
    bstack11l1l11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩὊ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111111l111_opy_(self):
    bstack1llllll11l11_opy_ = bstack11l1l11_opy_ (u"ࠪࠫὋ")
    bstack1lllllll1l11_opy_ = sys.platform
    bstack1llllll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪὌ")
    if re.match(bstack11l1l11_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧὍ"), bstack1lllllll1l11_opy_) != None:
      bstack1llllll11l11_opy_ = bstack11l11llll1l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢ὎")
      self.bstack1llllll11l1l_opy_ = bstack11l1l11_opy_ (u"ࠧ࡮ࡣࡦࠫ὏")
    elif re.match(bstack11l1l11_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨὐ"), bstack1lllllll1l11_opy_) != None:
      bstack1llllll11l11_opy_ = bstack11l11llll1l_opy_ + bstack11l1l11_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥὑ")
      bstack1llllll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨὒ")
      self.bstack1llllll11l1l_opy_ = bstack11l1l11_opy_ (u"ࠫࡼ࡯࡮ࠨὓ")
    else:
      bstack1llllll11l11_opy_ = bstack11l11llll1l_opy_ + bstack11l1l11_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣὔ")
      self.bstack1llllll11l1l_opy_ = bstack11l1l11_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬὕ")
    return bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_
  def bstack1lllllll11ll_opy_(self):
    try:
      bstack1lllll1ll11l_opy_ = [os.path.join(expanduser(bstack11l1l11_opy_ (u"ࠢࡿࠤὖ")), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨὗ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllll1ll11l_opy_:
        if(self.bstack1llllll1111l_opy_(path)):
          return path
      raise bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨ὘")
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧὙ").format(e))
  def bstack1llllll1111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll11ll11_opy_(self, bstack1llllll1ll1l_opy_):
    return os.path.join(bstack1llllll1ll1l_opy_, self.bstack1111lllll11_opy_ + bstack11l1l11_opy_ (u"ࠦ࠳࡫ࡴࡢࡩࠥ὚"))
  def bstack1lllll1ll1ll_opy_(self, bstack1llllll1ll1l_opy_, bstack1lllll1ll1l1_opy_):
    if not bstack1lllll1ll1l1_opy_: return
    try:
      bstack11111111ll1_opy_ = self.bstack1lllll11ll11_opy_(bstack1llllll1ll1l_opy_)
      with open(bstack11111111ll1_opy_, bstack11l1l11_opy_ (u"ࠧࡽࠢὛ")) as f:
        f.write(bstack1lllll1ll1l1_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡓࡢࡸࡨࡨࠥࡴࡥࡸࠢࡈࡘࡦ࡭ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠥ὜"))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡶ࡫ࡩࠥ࡫ࡴࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢὝ").format(e))
  def bstack1lllll11llll_opy_(self, bstack1llllll1ll1l_opy_):
    try:
      bstack11111111ll1_opy_ = self.bstack1lllll11ll11_opy_(bstack1llllll1ll1l_opy_)
      if os.path.exists(bstack11111111ll1_opy_):
        with open(bstack11111111ll1_opy_, bstack11l1l11_opy_ (u"ࠣࡴࠥ὞")) as f:
          bstack1lllll1ll1l1_opy_ = f.read().strip()
          return bstack1lllll1ll1l1_opy_ if bstack1lllll1ll1l1_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡉ࡙ࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧὟ").format(e))
  def bstack1111111ll1l_opy_(self, bstack1llllll1ll1l_opy_, bstack1llllll11l11_opy_):
    bstack1llllllll11l_opy_ = self.bstack1lllll11llll_opy_(bstack1llllll1ll1l_opy_)
    if bstack1llllllll11l_opy_:
      try:
        bstack111111111l1_opy_ = self.bstack1lllllllll1l_opy_(bstack1llllllll11l_opy_, bstack1llllll11l11_opy_)
        if not bstack111111111l1_opy_:
          self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡷࠥࡻࡰࠡࡶࡲࠤࡩࡧࡴࡦࠢࠫࡉ࡙ࡧࡧࠡࡷࡱࡧ࡭ࡧ࡮ࡨࡧࡧ࠭ࠧὠ"))
          return True
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡓ࡫ࡷࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡹࡵࡪࡡࡵࡧࠥὡ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡧࡱࡵࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦὢ").format(e))
    return False
  def bstack1lllllllll1l_opy_(self, bstack1llllllll11l_opy_, bstack1llllll11l11_opy_):
    try:
      headers = {
        bstack11l1l11_opy_ (u"ࠨࡉࡧ࠯ࡑࡳࡳ࡫࠭ࡎࡣࡷࡧ࡭ࠨὣ"): bstack1llllllll11l_opy_
      }
      response = bstack11lll11l11_opy_(bstack11l1l11_opy_ (u"ࠧࡈࡇࡗࠫὤ"), bstack1llllll11l11_opy_, {}, {bstack11l1l11_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤὥ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹ࠺ࠡࡽࢀࠦὦ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l1l1_opy_, stage=STAGE.bstack111llllll_opy_)
  def bstack11111111l11_opy_(self, bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_):
    try:
      bstack1llllllll111_opy_ = self.bstack1lllllll11ll_opy_()
      bstack1111111ll11_opy_ = os.path.join(bstack1llllllll111_opy_, bstack11l1l11_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ὧ"))
      bstack111111111ll_opy_ = os.path.join(bstack1llllllll111_opy_, bstack1llllll1l1l1_opy_)
      if self.bstack1111111ll1l_opy_(bstack1llllllll111_opy_, bstack1llllll11l11_opy_): # if bstack1lllll1ll111_opy_, bstack1lllll1llll_opy_ bstack1lllll1ll1l1_opy_ is bstack1llllll11lll_opy_ to bstack111l1l111l1_opy_ version available (response 304)
        if os.path.exists(bstack111111111ll_opy_):
          self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨὨ").format(bstack111111111ll_opy_))
          return bstack111111111ll_opy_
        if os.path.exists(bstack1111111ll11_opy_):
          self.logger.info(bstack11l1l11_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥὩ").format(bstack1111111ll11_opy_))
          return self.bstack1lllllll1l1l_opy_(bstack1111111ll11_opy_, bstack1llllll1l1l1_opy_)
      self.logger.info(bstack11l1l11_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦὪ").format(bstack1llllll11l11_opy_))
      response = bstack11lll11l11_opy_(bstack11l1l11_opy_ (u"ࠧࡈࡇࡗࠫὫ"), bstack1llllll11l11_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll1l1ll1_opy_ = response.headers.get(bstack11l1l11_opy_ (u"ࠣࡇࡗࡥ࡬ࠨὬ"), bstack11l1l11_opy_ (u"ࠤࠥὭ"))
        if bstack1lllll1l1ll1_opy_:
          self.bstack1lllll1ll1ll_opy_(bstack1llllllll111_opy_, bstack1lllll1l1ll1_opy_)
        with open(bstack1111111ll11_opy_, bstack11l1l11_opy_ (u"ࠪࡻࡧ࠭Ὦ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l1l11_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤὯ").format(bstack1111111ll11_opy_))
        return self.bstack1lllllll1l1l_opy_(bstack1111111ll11_opy_, bstack1llllll1l1l1_opy_)
      else:
        raise(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣὰ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢά").format(e))
  def bstack1lllll11ll1l_opy_(self, bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_):
    try:
      retry = 2
      bstack111111111ll_opy_ = None
      bstack1llllll1llll_opy_ = False
      while retry > 0:
        bstack111111111ll_opy_ = self.bstack11111111l11_opy_(bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_)
        bstack1llllll1llll_opy_ = self.bstack1lllllllllll_opy_(bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_, bstack111111111ll_opy_)
        if bstack1llllll1llll_opy_:
          break
        retry -= 1
      return bstack111111111ll_opy_, bstack1llllll1llll_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦὲ").format(e))
    return bstack111111111ll_opy_, False
  def bstack1lllllllllll_opy_(self, bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_, bstack111111111ll_opy_, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 1:
      return False
    if bstack111111111ll_opy_ == None or os.path.exists(bstack111111111ll_opy_) == False:
      self.logger.warn(bstack11l1l11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨέ"))
      return False
    bstack11111111l1l_opy_ = bstack11l1l11_opy_ (u"ࡴࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫ࠣࡠࡩ࠱࡜࠯࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭ࠥὴ")
    command = bstack11l1l11_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩή").format(bstack111111111ll_opy_)
    bstack1lllll11lll1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11111111l1l_opy_, bstack1lllll11lll1_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥὶ"))
      return False
  def bstack1lllllll1l1l_opy_(self, bstack1111111ll11_opy_, bstack1llllll1l1l1_opy_):
    try:
      working_dir = os.path.dirname(bstack1111111ll11_opy_)
      shutil.unpack_archive(bstack1111111ll11_opy_, working_dir)
      bstack111111111ll_opy_ = os.path.join(working_dir, bstack1llllll1l1l1_opy_)
      os.chmod(bstack111111111ll_opy_, 0o755)
      return bstack111111111ll_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨί"))
  def bstack1lllll1lll1l_opy_(self):
    try:
      bstack1lllllll1lll_opy_ = self.config.get(bstack11l1l11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬὸ"))
      bstack1lllll1lll1l_opy_ = bstack1lllllll1lll_opy_ or (bstack1lllllll1lll_opy_ is None and self.bstack11llll1111_opy_)
      if not bstack1lllll1lll1l_opy_ or self.config.get(bstack11l1l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪό"), None) not in bstack11l11l1l11l_opy_:
        return False
      self.bstack1l1l1ll11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥὺ").format(e))
  def bstack1lllllllll11_opy_(self):
    try:
      bstack1lllllllll11_opy_ = self.percy_capture_mode
      return bstack1lllllllll11_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥύ").format(e))
  def init(self, bstack11llll1111_opy_, config, logger):
    self.bstack11llll1111_opy_ = bstack11llll1111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1lll1l_opy_():
      return
    self.bstack1llllll111ll_opy_ = config.get(bstack11l1l11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩὼ"), {})
    self.percy_capture_mode = config.get(bstack11l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧώ"))
    try:
      bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_ = self.bstack1111111l111_opy_()
      self.bstack1111lllll11_opy_ = bstack1llllll1l1l1_opy_
      bstack111111111ll_opy_, bstack1llllll1llll_opy_ = self.bstack1lllll11ll1l_opy_(bstack1llllll11l11_opy_, bstack1llllll1l1l1_opy_)
      if bstack1llllll1llll_opy_:
        self.binary_path = bstack111111111ll_opy_
        thread = Thread(target=self.bstack1lllll1l11l1_opy_)
        thread.start()
      else:
        self.bstack1llllllllll1_opy_ = True
        self.logger.error(bstack11l1l11_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤ὾").format(bstack111111111ll_opy_))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὿").format(e))
  def bstack1lllll1l111l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡪࠫᾀ"), bstack11l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫᾁ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨᾂ").format(logfile))
      self.bstack1lllll1lll11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾃ").format(e))
  @measure(event_name=EVENTS.bstack11l11llll11_opy_, stage=STAGE.bstack111llllll_opy_)
  def bstack1lllll1l11l1_opy_(self):
    bstack1lllll1l1111_opy_ = self.bstack1lllll1llll1_opy_()
    if bstack1lllll1l1111_opy_ == None:
      self.bstack1llllllllll1_opy_ = True
      self.logger.error(bstack11l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢᾄ"))
      return False
    bstack1lllll11l1ll_opy_ = [bstack11l1l11_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨᾅ") if self.bstack11llll1111_opy_ else bstack11l1l11_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪᾆ")]
    bstack11111l1111l_opy_ = self.bstack1lllll1l11ll_opy_()
    if bstack11111l1111l_opy_ != None:
      bstack1lllll11l1ll_opy_.append(bstack11l1l11_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨᾇ").format(bstack11111l1111l_opy_))
    env = os.environ.copy()
    env[bstack11l1l11_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨᾈ")] = bstack1lllll1l1111_opy_
    env[bstack11l1l11_opy_ (u"ࠤࡗࡌࡤࡈࡕࡊࡎࡇࡣ࡚࡛ࡉࡅࠤᾉ")] = os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᾊ"), bstack11l1l11_opy_ (u"ࠫࠬᾋ"))
    bstack11111111111_opy_ = [self.binary_path]
    self.bstack1lllll1l111l_opy_()
    self.bstack1111111111l_opy_ = self.bstack1lllllll111l_opy_(bstack11111111111_opy_ + bstack1lllll11l1ll_opy_, env)
    self.logger.debug(bstack11l1l11_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᾌ"))
    bstack1llllll111l1_opy_ = 0
    while self.bstack1111111111l_opy_.poll() == None:
      bstack1lllll1lllll_opy_ = self.bstack1llllllll1l1_opy_()
      if bstack1lllll1lllll_opy_:
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᾍ"))
        self.bstack1llllllll1ll_opy_ = True
        return True
      bstack1llllll111l1_opy_ += 1
      self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᾎ").format(bstack1llllll111l1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨᾏ").format(bstack1llllll111l1_opy_))
    self.bstack1llllllllll1_opy_ = True
    return False
  def bstack1llllllll1l1_opy_(self, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 10:
      return False
    try:
      bstack1llllll1l1ll_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩᾐ"), bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫᾑ"))
      bstack1lllllll11l1_opy_ = bstack1llllll1l1ll_opy_ + bstack11l11l1l1ll_opy_
      response = requests.get(bstack1lllllll11l1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪᾒ"), {}).get(bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨᾓ"), None)
      return True
    except:
      self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣ࡬ࡪࡧ࡬ࡵࡪࠣࡧ࡭࡫ࡣ࡬ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦᾔ"))
      return False
  def bstack1lllll1llll1_opy_(self):
    bstack1111111l11l_opy_ = bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࠫᾕ") if self.bstack11llll1111_opy_ else bstack11l1l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᾖ")
    bstack1llllll1lll1_opy_ = bstack11l1l11_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾗ") if self.config.get(bstack11l1l11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᾘ")) is None else True
    bstack11ll111l11l_opy_ = bstack11l1l11_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠩࡴࡪࡸࡣࡺ࠿ࡾࢁࠧᾙ").format(self.config[bstack11l1l11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᾚ")], bstack1111111l11l_opy_, bstack1llllll1lll1_opy_)
    if self.percy_capture_mode:
      bstack11ll111l11l_opy_ += bstack11l1l11_opy_ (u"ࠨࠦࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࡂࢁࡽࠣᾛ").format(self.percy_capture_mode)
    uri = bstack1l11l1111_opy_(bstack11ll111l11l_opy_)
    try:
      response = bstack11lll11l11_opy_(bstack11l1l11_opy_ (u"ࠧࡈࡇࡗࠫᾜ"), uri, {}, {bstack11l1l11_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᾝ"): (self.config[bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᾞ")], self.config[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᾟ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1l1ll11_opy_ = data.get(bstack11l1l11_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᾠ"))
        self.percy_capture_mode = data.get(bstack11l1l11_opy_ (u"ࠬࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࠪᾡ"))
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᾢ")] = str(self.bstack1l1l1ll11_opy_)
        os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᾣ")] = str(self.percy_capture_mode)
        if bstack1llllll1lll1_opy_ == bstack11l1l11_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᾤ") and str(self.bstack1l1l1ll11_opy_).lower() == bstack11l1l11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᾥ"):
          self.bstack1111l1lll_opy_ = True
        if bstack11l1l11_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾦ") in data:
          return data[bstack11l1l11_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾧ")]
        else:
          raise bstack11l1l11_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬᾨ").format(data)
      else:
        raise bstack11l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨᾩ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣᾪ").format(e))
  def bstack1lllll1l11ll_opy_(self):
    bstack1lllll1l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦᾫ"))
    try:
      if bstack11l1l11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾬ") not in self.bstack1llllll111ll_opy_:
        self.bstack1llllll111ll_opy_[bstack11l1l11_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾭ")] = 2
      with open(bstack1lllll1l1l1l_opy_, bstack11l1l11_opy_ (u"ࠫࡼ࠭ᾮ")) as fp:
        json.dump(self.bstack1llllll111ll_opy_, fp)
      return bstack1lllll1l1l1l_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾯ").format(e))
  def bstack1lllllll111l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll11l1l_opy_ == bstack11l1l11_opy_ (u"࠭ࡷࡪࡰࠪᾰ"):
        bstack1111111l1ll_opy_ = [bstack11l1l11_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᾱ"), bstack11l1l11_opy_ (u"ࠨ࠱ࡦࠫᾲ")]
        cmd = bstack1111111l1ll_opy_ + cmd
      cmd = bstack11l1l11_opy_ (u"ࠩࠣࠫᾳ").join(cmd)
      self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᾴ").format(cmd))
      with open(self.bstack1lllll1lll11_opy_, bstack11l1l11_opy_ (u"ࠦࡦࠨ᾵")) as bstack1lllll1l1lll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll1l1lll_opy_, text=True, stderr=bstack1lllll1l1lll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllllllll1_opy_ = True
      self.logger.error(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᾶ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllll1ll_opy_:
        self.logger.info(bstack11l1l11_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᾷ"))
        cmd = [self.binary_path, bstack11l1l11_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᾸ")]
        self.bstack1lllllll111l_opy_(cmd)
        self.bstack1llllllll1ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾹ").format(cmd, e))
  def bstack1111l1l1l1_opy_(self):
    if not self.bstack1l1l1ll11_opy_:
      return
    try:
      bstack1111111l1l1_opy_ = 0
      while not self.bstack1llllllll1ll_opy_ and bstack1111111l1l1_opy_ < self.bstack1llllll11111_opy_:
        if self.bstack1llllllllll1_opy_:
          self.logger.info(bstack11l1l11_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᾺ"))
          return
        time.sleep(1)
        bstack1111111l1l1_opy_ += 1
      os.environ[bstack11l1l11_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩΆ")] = str(self.bstack11111111lll_opy_())
      self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧᾼ"))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᾽").format(e))
  def bstack11111111lll_opy_(self):
    if self.bstack11llll1111_opy_:
      return
    try:
      bstack1lllll1l1l11_opy_ = [platform[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫι")].lower() for platform in self.config.get(bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᾿"), [])]
      bstack1llllll1l111_opy_ = sys.maxsize
      bstack1lllllll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠨࠩ῀")
      for browser in bstack1lllll1l1l11_opy_:
        if browser in self.bstack1llllll11ll1_opy_:
          bstack1llllll1ll11_opy_ = self.bstack1llllll11ll1_opy_[browser]
        if bstack1llllll1ll11_opy_ < bstack1llllll1l111_opy_:
          bstack1llllll1l111_opy_ = bstack1llllll1ll11_opy_
          bstack1lllllll1ll1_opy_ = browser
      return bstack1lllllll1ll1_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ῁").format(e))
  @classmethod
  def bstack1l1l1111l1_opy_(self):
    return os.getenv(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨῂ"), bstack11l1l11_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪῃ")).lower()
  @classmethod
  def bstack11111llll_opy_(self):
    return os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩῄ"), bstack11l1l11_opy_ (u"࠭ࠧ῅"))
  @classmethod
  def bstack11llll1ll1l_opy_(cls, value):
    cls.bstack1111l1lll_opy_ = value
  @classmethod
  def bstack1lllllll1111_opy_(cls):
    return cls.bstack1111l1lll_opy_
  @classmethod
  def bstack11lllll1l11_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1l11l_opy_(cls):
    return cls.percy_build_id