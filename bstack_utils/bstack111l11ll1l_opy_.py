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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11llll_opy_, bstack11l11l1l1l1_opy_, bstack11l1l1111l1_opy_
import tempfile
import json
bstack11111l11l11_opy_ = os.getenv(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡇࡠࡈࡌࡐࡊࠨề"), None) or os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪ࠲ࡱࡵࡧࠣỂ"))
bstack11111l1ll1l_opy_ = os.path.join(bstack11l1l11_opy_ (u"ࠢ࡭ࡱࡪࠦể"), bstack11l1l11_opy_ (u"ࠨࡵࡧ࡯࠲ࡩ࡬ࡪ࠯ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬỄ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l1l11_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬễ"),
      datefmt=bstack11l1l11_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨỆ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1l11l11_opy_():
  bstack11111l1l1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡈࡊࡈࡕࡈࠤệ"), bstack11l1l11_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦỈ"))
  return logging.DEBUG if bstack11111l1l1l1_opy_.lower() == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦỉ") else logging.INFO
def bstack1ll11ll1l1l_opy_():
  global bstack11111l11l11_opy_
  if os.path.exists(bstack11111l11l11_opy_):
    os.remove(bstack11111l11l11_opy_)
  if os.path.exists(bstack11111l1ll1l_opy_):
    os.remove(bstack11111l1ll1l_opy_)
def bstack11l1ll1l11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111ll1l11_opy_ = log_level
  if bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩỊ") in config and config[bstack11l1l11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪị")] in bstack11l11l1l1l1_opy_:
    bstack11111ll1l11_opy_ = bstack11l11l1l1l1_opy_[config[bstack11l1l11_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫỌ")]]
  if config.get(bstack11l1l11_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬọ"), False):
    logging.getLogger().setLevel(bstack11111ll1l11_opy_)
    return bstack11111ll1l11_opy_
  global bstack11111l11l11_opy_
  bstack11l1ll1l11_opy_()
  bstack111111lllll_opy_ = logging.Formatter(
    fmt=bstack11l1l11_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧỎ"),
    datefmt=bstack11l1l11_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪỏ"),
  )
  bstack11111l11ll1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l11l11_opy_)
  file_handler.setFormatter(bstack111111lllll_opy_)
  bstack11111l11ll1_opy_.setFormatter(bstack111111lllll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l11ll1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l1l11_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࡷ࡫࡭ࡰࡶࡨ࠲ࡷ࡫࡭ࡰࡶࡨࡣࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨỐ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l11ll1_opy_.setLevel(bstack11111ll1l11_opy_)
  logging.getLogger().addHandler(bstack11111l11ll1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111ll1l11_opy_
def bstack11111l1l11l_opy_(config):
  try:
    bstack11111ll1111_opy_ = set(bstack11l1l1111l1_opy_)
    bstack11111l111ll_opy_ = bstack11l1l11_opy_ (u"ࠧࠨố")
    with open(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫỒ")) as bstack11111ll1ll1_opy_:
      bstack11111ll111l_opy_ = bstack11111ll1ll1_opy_.read()
      bstack11111l111ll_opy_ = re.sub(bstack11l1l11_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠧ࠳࠰ࠤ࡝ࡰࠪồ"), bstack11l1l11_opy_ (u"ࠪࠫỔ"), bstack11111ll111l_opy_, flags=re.M)
      bstack11111l111ll_opy_ = re.sub(
        bstack11l1l11_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄ࠮ࠧổ") + bstack11l1l11_opy_ (u"ࠬࢂࠧỖ").join(bstack11111ll1111_opy_) + bstack11l1l11_opy_ (u"࠭ࠩ࠯ࠬࠧࠫỗ"),
        bstack11l1l11_opy_ (u"ࡲࠨ࡞࠵࠾ࠥࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩỘ"),
        bstack11111l111ll_opy_, flags=re.M | re.I
      )
    def bstack11111ll11ll_opy_(dic):
      bstack11111l1lll1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111ll1111_opy_:
          bstack11111l1lll1_opy_[key] = bstack11l1l11_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬộ")
        else:
          if isinstance(value, dict):
            bstack11111l1lll1_opy_[key] = bstack11111ll11ll_opy_(value)
          else:
            bstack11111l1lll1_opy_[key] = value
      return bstack11111l1lll1_opy_
    bstack11111l1lll1_opy_ = bstack11111ll11ll_opy_(config)
    return {
      bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬỚ"): bstack11111l111ll_opy_,
      bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡴࡡ࡭ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ớ"): json.dumps(bstack11111l1lll1_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l11111_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠫࡱࡵࡧࠨỜ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1111l_opy_ = os.path.join(log_dir, bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠭ờ"))
  if not os.path.exists(bstack11111l1111l_opy_):
    bstack11111l111l1_opy_ = {
      bstack11l1l11_opy_ (u"ࠨࡩ࡯࡫ࡳࡥࡹ࡮ࠢỞ"): str(inipath),
      bstack11l1l11_opy_ (u"ࠢࡳࡱࡲࡸࡵࡧࡴࡩࠤở"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l1l11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧỠ")), bstack11l1l11_opy_ (u"ࠩࡺࠫỡ")) as bstack11111l11lll_opy_:
      bstack11111l11lll_opy_.write(json.dumps(bstack11111l111l1_opy_))
def bstack11111l1ll11_opy_():
  try:
    bstack11111l1111l_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠪࡰࡴ࡭ࠧỢ"), bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪợ"))
    if os.path.exists(bstack11111l1111l_opy_):
      with open(bstack11111l1111l_opy_, bstack11l1l11_opy_ (u"ࠬࡸࠧỤ")) as bstack11111l11lll_opy_:
        bstack11111l1l111_opy_ = json.load(bstack11111l11lll_opy_)
      return bstack11111l1l111_opy_.get(bstack11l1l11_opy_ (u"࠭ࡩ࡯࡫ࡳࡥࡹ࡮ࠧụ"), bstack11l1l11_opy_ (u"ࠧࠨỦ")), bstack11111l1l111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡴࡲࡳࡹࡶࡡࡵࡪࠪủ"), bstack11l1l11_opy_ (u"ࠩࠪỨ"))
  except:
    pass
  return None, None
def bstack11111ll1l1l_opy_():
  try:
    bstack11111l1111l_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠪࡰࡴ࡭ࠧứ"), bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪỪ"))
    if os.path.exists(bstack11111l1111l_opy_):
      os.remove(bstack11111l1111l_opy_)
  except:
    pass
def bstack1ll11l11_opy_(config):
  try:
    from bstack_utils.helper import bstack111ll1ll_opy_, bstack1lllllll11_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l11l11_opy_
    if config.get(bstack11l1l11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧừ"), False):
      return
    uuid = os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỬ")) if os.getenv(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬử")) else bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥỮ"))
    if not uuid or uuid == bstack11l1l11_opy_ (u"ࠩࡱࡹࡱࡲࠧữ"):
      return
    bstack11111l1llll_opy_ = [bstack11l1l11_opy_ (u"ࠪࡶࡪࡷࡵࡪࡴࡨࡱࡪࡴࡴࡴ࠰ࡷࡼࡹ࠭Ự"), bstack11l1l11_opy_ (u"ࠫࡕ࡯ࡰࡧ࡫࡯ࡩࠬự"), bstack11l1l11_opy_ (u"ࠬࡶࡹࡱࡴࡲ࡮ࡪࡩࡴ࠯ࡶࡲࡱࡱ࠭Ỳ"), bstack11111l11l11_opy_, bstack11111l1ll1l_opy_]
    bstack11111l1l1ll_opy_, root_path = bstack11111l1ll11_opy_()
    if bstack11111l1l1ll_opy_ != None:
      bstack11111l1llll_opy_.append(bstack11111l1l1ll_opy_)
    if root_path != None:
      bstack11111l1llll_opy_.append(os.path.join(root_path, bstack11l1l11_opy_ (u"࠭ࡣࡰࡰࡩࡸࡪࡹࡴ࠯ࡲࡼࠫỳ")))
    bstack11l1ll1l11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭࡭ࡱࡪࡷ࠲࠭Ỵ") + uuid + bstack11l1l11_opy_ (u"ࠨ࠰ࡷࡥࡷ࠴ࡧࡻࠩỵ"))
    with tarfile.open(output_file, bstack11l1l11_opy_ (u"ࠤࡺ࠾࡬ࢀࠢỶ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1llll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1l11l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l11l1l_opy_ = data.encode()
        tarinfo.size = len(bstack11111l11l1l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l11l1l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l1l11_opy_ (u"ࠪࡨࡦࡺࡡࠨỷ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l1l11_opy_ (u"ࠫࡷࡨࠧỸ")), bstack11l1l11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࠲࡭ࡺࡪࡲࠪỹ")),
        bstack11l1l11_opy_ (u"࠭ࡣ࡭࡫ࡨࡲࡹࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨỺ"): uuid
      }
    )
    bstack11111ll11l1_opy_ = bstack1lllllll11_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠢࡢࡲ࡬ࡷࠧỻ"), bstack11l1l11_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣỼ"), bstack11l1l11_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࠤỽ")], bstack11l1l11llll_opy_)
    response = requests.post(
      bstack11l1l11_opy_ (u"ࠥࡿࢂ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦỾ").format(bstack11111ll11l1_opy_),
      data=multipart_data,
      headers={bstack11l1l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪỿ"): multipart_data.content_type},
      auth=(config[bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧἀ")], config[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩἁ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱ࡮ࡲࡥࡩࠦ࡬ࡰࡩࡶ࠾ࠥ࠭ἂ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l1l11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࡀࠧἃ") + str(e))
  finally:
    try:
      bstack1ll11ll1l1l_opy_()
      bstack11111ll1l1l_opy_()
    except:
      pass